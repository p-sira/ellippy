# Changelog

## 1.2.0

**New functions**

- `ellipke(m)`: simultaneous computation of K(m) and E(m).
- `cel3(kc, p)`: complete elliptic integral of the third kind in Bulirsch form.

**Improvements**

- Upgrade PyO3 from 0.26.0 to 0.29.3 and numpy from 0.26.0 to 0.29.0.
- Skip GIL release for single-element array calls. `py.detach()` has a fixed overhead that exceeds the cost of the computation itself for small inputs; single-element arrays now bypass it.
- Add `gil_used = false` to `#[pymodule]` for forward compatibility with free-threading Python (PEP 703).
- Add `strip = true` to the release profile to reduce the size of the shared library.
- **FFI threshold tuning for `cel3`**: `ellip-rayon`'s built-in parallelism threshold is calibrated at the pure-Rust level (~8k elements). A new `bench_threshold` binary that simulates the `PyArray1::from_vec` O(n) copy cost reveals the true break-even at **~10k elements** (+25%). This exceeds our 20% tolerance band, so `cel3` now uses a hand-written `CEL3_FFI_THRESHOLD = 10_000` guard: calls with ≤10k elements run sequentially, avoiding Rayon scheduling overhead and the redundant buffer copy. `ellipke`'s FFI crossover matches its Rust-only threshold (~30k) so no override is needed there.

## 1.1.3

**Improvements**

- Improve performance by using LTO, opt-level 3, and codegen-units 1.

## 1.1.2

**Improvements**

- Improve performance of `heuman_lambda`.
- Update package metadata.

## 0.1.0

- First release of EllipPy, consistent with ellip v0.5.1.
