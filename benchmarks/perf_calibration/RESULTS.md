# Reviewed calibration results

Reference: AMD Ryzen 5 4600H, Linux x86-64, 12 Rayon workers, CPython 3.13.3,
NumPy 2.4.2, release build with LTO. These are conservative reference defaults,
not optimal thresholds for every input layout or machine.

The original discovery sweep measured ordinary and near-boundary inputs with independent
Rust and GIL policies, then extended, refined and validated alternate layouts.
For each function, the initial cutover rounded the largest confirmed contiguous
float64 candidate across both distributions and GIL contexts up to a power of
two. A full automatic-path check then exposed conversion-heavy regressions.
Those functions were raised by a further factor of two, or four for the
affected `cel` family, and rechecked with longer 5 ms timing windows.

GIL latency comparisons were often inconclusive. The selected policy detaches
at the Rayon cutover to avoid transition overhead in smaller serial batches
and allow background Python threads to run during parallel work. This is a
responsiveness choice, not a claim of a consistently faster GIL transition.
Retained large-call probes showed no background progress; detached probes
showed progress for the sampled kernels.

| Function | First Rayon size | First detach size |
|---|---:|---:|
| `cel` | 8,192 | 8,192 |
| `cel1` | 16,384 | 16,384 |
| `cel2` | 8,192 | 8,192 |
| `cel3` | 8,192 | 8,192 |
| `el1` | 4,096 | 4,096 |
| `el2` | 32,768 | 32,768 |
| `el3` | 4,096 | 4,096 |
| `ellipd` | 8,192 | 8,192 |
| `ellipdinc` | 4,096 | 4,096 |
| `ellipe` | 16,384 | 16,384 |
| `ellipeinc` | 1,024 | 1,024 |
| `ellipf` | 1,024 | 1,024 |
| `ellipk` | 65,536 | 65,536 |
| `ellipke` | 32,768 | 32,768 |
| `ellippi` | 1,024 | 1,024 |
| `ellippiinc` | 32,768 | 32,768 |
| `ellippiinc_bulirsch` | 1,024 | 1,024 |
| `elliprc` | 8,192 | 8,192 |
| `elliprd` | 2,048 | 2,048 |
| `elliprf` | 2,048 | 2,048 |
| `elliprg` | 4,096 | 4,096 |
| `elliprj` | 1,024 | 1,024 |
| `heuman_lambda` | 512 | 512 |
| `jacobi_zeta` | 1,024 | 1,024 |

## Regenerated candidate selection

The regenerated `candidates.md` matches the completed Ellip 1.2.3 report
`python-path-20261014-205328-118827`, containing 31,689 timing records with
12 Rayon workers and 5 ms sample windows. Reviewed selections, source/binary
hashes, report hash, and candidate evidence are preserved in
[reviewed_candidates.json](reviewed_candidates.json).

A function is eligible for a new cutover when all four contiguous float64
Rayon comparisons have confirmed crossovers: both input distributions under
both retained and detached GIL execution. The selected cutover rounds the
largest confirmed Rayon candidate across every layout up to a power of two.
This uses late confirmed list-input crossovers instead of lowering cutovers
solely from float64 results. `ellipk` retains 65,536 because its detached,
uniform float64 comparison is inconclusive.

This changes 18 functions: 15 cutovers decrease, while `el2`, `ellipdinc`, and
`ellippiinc` increase to account for confirmed late list-input crossovers.
Other cutovers remain unchanged. `inconclusive` and `no_crossover` rows do not
supply a threshold, and unresolved layouts remain outside the confirmed
performance evidence. These constants do not guarantee faster execution for
those layouts.

Detachment remains a responsiveness policy at the selected Rayon cutover.
Most GIL latency comparisons remain inconclusive. `ellipdinc` has confirmed
float64 candidates at 4,096 for both distributions, matching its new cutover.
The other partial GIL candidates are not adopted as global latency thresholds.
Changing the Rayon policy also changes the automatic execution used by the GIL
comparison. The supplied benchmark is the basis for this adjustment; no
additional timing run is used to override its candidates. All 253 calibration
tests passed with the revised compiled cutovers, including boundary and
numerical checks.

## Historical validation (Ellip 1.2.0)

The three original runs used Ellip 1.2.0 and contain 53,949 timing records. At the selected cutovers,
the median automatic/forced-serial latency ratio across 192 layout/distribution
comparisons was 0.667. This aggregate does not imply a gain in every workload.
5 comparisons remained more than 5% slower than forced serial execution:

| Function | Layout | Distribution | Automatic / serial |
|---|---|---|---:|
| `cel` | contiguous_f32 | uniform | 1.730 |
| `cel` | python_list | uniform | 1.274 |
| `ellipeinc` | python_list | near_boundary | 1.193 |
| `ellipke` | python_list | uniform | 1.113 |
| `elliprf` | python_list | near_boundary | 1.288 |

In these cases, latency varied across policies that execute the same Rust/GIL
branches. Conversion and scheduling costs limit the benefit, and the host was
not established to be idle. Treat these comparisons as unresolved; rerun on
a quiet target before claiming optimal cutovers for lists or copied arrays.
The ratio compares with forced serial/retain, not the previous EllipPy release.
The defaults prioritize avoiding premature Rayon dispatch for small batches
and retaining Python-thread responsiveness for large ones. Contiguous float64
inputs can benefit from earlier parallel cutovers than these conservative defaults.

## Pre-adjustment validation (Ellip 1.2.3)

A full compiled-cutover check used 5 ms sample windows, followed by a 10 ms
recheck of six functions with slower layout comparisons. Together these runs
contain 14,616 timing records. Each cutover comparison below uses the latest
run for that function; earlier measurements are preserved separately.

The first run found a consistent list-input regression for `elliprc` at 16,384
and improvement at 32,768. Its Rayon and detach cutovers were raised to 32,768.
The longer recheck remained variable, including for policies taking identical
execution branches. This supports a conservative increase but does not establish
an optimal crossover. Other constants retain the historical reference choices.

Across 192 selected-cutover layout/distribution comparisons, the median
automatic/forced-serial latency ratio is 0.701. Nineteen comparisons remain
more than 5% slower:

| Function | Layout | Distribution | Automatic / serial |
|---|---|---|---:|
| `cel` | strided_f64 | near_boundary | 1.117 |
| `el2` | contiguous_f32 | uniform | 1.340 |
| `el2` | python_list | near_boundary | 1.273 |
| `el2` | python_list | uniform | 1.374 |
| `el2` | strided_f64 | near_boundary | 1.407 |
| `el2` | strided_f64 | uniform | 1.781 |
| `ellipd` | contiguous_f32 | near_boundary | 1.154 |
| `ellipd` | contiguous_f32 | uniform | 1.277 |
| `ellipd` | python_list | near_boundary | 1.158 |
| `ellipd` | python_list | uniform | 1.664 |
| `ellipd` | strided_f64 | uniform | 1.485 |
| `ellipke` | contiguous_f32 | uniform | 2.084 |
| `ellipke` | contiguous_f64 | uniform | 1.240 |
| `ellipke` | python_list | near_boundary | 1.067 |
| `ellipke` | python_list | uniform | 1.485 |
| `ellipke` | strided_f64 | uniform | 2.002 |
| `ellippi` | python_list | near_boundary | 1.363 |
| `ellippi` | python_list | uniform | 1.389 |
| `elliprc` | python_list | uniform | 1.111 |

The aggregate mixes the full run with the latest recheck and compares against
forced serial/retain, not the previous release. The host was not established
to be idle. Larger timing windows did not remove variability. These comparisons
remain unresolved; a quiet-target calibration is required before claiming
stable gains across all layouts. No further thresholds were raised from this
noisy recheck.

All branch and numerical checks passed. In the full run, detached probes allowed
background-thread progress for all 24 kernels; retained probes showed none.
This supports the responsiveness policy independently of latency optimality.

## Reproduce and inspect

Commands and raw report hashes are recorded in the regenerated
[candidate review](reviewed_candidates.json), the earlier
[Ellip 1.2.3 review](reviewed_results_ellip_1_2_3.json) and the historical
[Ellip 1.2.0 review](reviewed_results.json).
The full raw reports remain under ignored `benchmark-results/`. The review
artifact preserves paired per-round medians at each selected cutover, compiled
thresholds, source and binary hashes, environment and command configuration.
Use the [calibration guide](README.md) for a fresh sweep or `--validate-defaults` run.

## Numerical verification

EllipPy now depends on the published Ellip 1.2.3 crate. The numerical fixture
submodule is pinned to `e43064e0100087819a37a1d2a0e8bf2b81895603`, the
source revision recorded in that crate's package metadata. Its Rust source
matches the published crate. Tests reuse its Wolfram CSVs with quoting enabled.
RJ bounds match Rust, including an absolute epsilon bound near principal-value
zeros. The regenerated RJ principal-value fixtures are included in this pin.

The RG failure for six permutations of `(0, f64::EPSILON, 16/9)` is resolved
by Ellip 1.2.3. Additional Python regressions exercise those inputs through scalar
calls and both automatic batch branches, at scales `2^-600`, `1`, and `2^600`.
Existing RG fixture bounds remain unchanged.
