# Python-path threshold calibration

EllipPy makes two independent batch decisions: whether to use Rayon and whether
to detach from the Python interpreter during Rust computation. The public
Python call is timed, including contiguous float64 conversion, FFI, allocation,
and conversion of the result (including both outputs of `ellipke`). Fixture
construction and policy instrumentation are outside the timing loop.

Dispatch lives in EllipPy's binding and calls the published `ellip` scalar
kernels in both branches. This lets Python-specific constants travel with the
wheel source without a custom `ellip-rayon` commit or local submodule edits.
Cargo.lock pins Ellip 1.2.3. The `vendor/ellip` submodule supplies numerical
test fixtures from the same published source revision; wheel builds use crates.io.
Normal builds contain no policy overrides or counters. The public Python API
is unchanged.

## Reproduce

From the repository root:

```sh
uv sync --dev
uv run maturin develop --release --locked --features threshold-calibration
RAYON_NUM_THREADS=12 uv run python benchmarks/perf_calibration/calibrate_thresholds.py --preflight
RAYON_NUM_THREADS=12 uv run python benchmarks/perf_calibration/calibrate_thresholds.py --dry-run
RAYON_NUM_THREADS=12 uv run python benchmarks/perf_calibration/calibrate_thresholds.py
uv run python benchmarks/perf_calibration/extract_thresholds.py benchmark-results/python-path-<run>/report.json --output candidates.md
```

Use the same explicit worker count for the entire run. Keep the machine idle;
CPU affinity, power settings, thread count, interpreter, NumPy version and
input distributions affect the result. Run separate calibrations for materially
different deployment targets. Calibration workers have process-global controls;
do not enable them in a concurrently used application.

Each policy gets a fresh subprocess. The sweep rotates and reverses policy order
between rounds and shuffles workloads deterministically. It verifies branch
counters and compares values with a forced serial reference before timing.
Instrumentation is disabled during measurements. Raw samples, round numbers,
actual compiled thresholds, binary hash, source hashes, dependency-lock hash,
Git state, CPU affinity and actual Rayon worker count are saved in `report.json`.
Failed runs retain partial records but have no completed candidate summary.

The seven policies include all four forced Rust/GIL combinations, automatic Rust
with each forced GIL policy, and fully automatic execution. `rayon` compares
serial versus parallel while retaining the GIL; `rayon_detached` repeats that
comparison while detached; `gil` compares automatic Rust with retain versus
detach. The background-thread responsiveness probe is separate from latency
measurements. Its progress counts include the entire public call, so they are
evidence about responsiveness, not a Rust-only GIL branch measurement.

After reviewing and updating `src/thresholds.rs`, rebuild the calibration
extension and verify the actual compiled cutovers:

```sh
uv run maturin develop --release --locked --features threshold-calibration
RAYON_NUM_THREADS=12 uv run python benchmarks/perf_calibration/calibrate_thresholds.py --validate-defaults
```

This mode tests each compiled cutover, the immediately preceding size, and
twice the cutover, across all four layouts and both distributions. It repeats
the seven policies with branch and numerical checks, then runs the separate
responsiveness probe. It does not extend or refine the grid.

## Interpret candidates

A switch candidate requires at least a 5% median reduction and a 5% win in at
least two-thirds of rounds at two neighboring sizes, with no reversal at larger
measured sizes. The runner extends unresolved sweeps up to `--max-size`, refines
the observed intervals, and validates neighboring sizes with float32, strided
arrays, and Python lists. `inconclusive` and `no_crossover` do not justify a
threshold. A candidate range describes the untested interval between a losing
size and the first confirmed winning size; review its upper end conservatively.

Thresholds in `src/thresholds.rs` are **first switch sizes**, using
`n >= threshold`. They are not PyMagba's `len > threshold` constants. A first
parallel size of 160 is stored as 160 here. `usize::MAX` disables an automatic
switch. Scalar calls bypass batch dispatch.

Review ordinary and near-boundary inputs together, both GIL contexts for Rayon,
and alternate layouts. Changing Rayon defaults changes the automatic path used
by the GIL comparison: rebuild and repeat that comparison before selecting GIL
thresholds. A latency comparison alone does not decide how long other Python
threads should be blocked. Keep responsiveness findings separate from speed
claims, and document any responsiveness-based detachment policy explicitly.

Reports remain under ignored `benchmark-results/`; commit reviewed results and
constants, not an automatic rewrite from one noisy sample. Publishing uses the
checked-in binding and Cargo lockfile and does not run calibration on CI hosts.

After calibration, rebuild the normal extension and verify that hooks are gone:

```sh
uv run maturin develop --release --locked
uv run python -c 'from ellippy import ellippy_binding as b; assert not hasattr(b, "_set_threshold_calibration")'
uv run pytest python/tests
```
