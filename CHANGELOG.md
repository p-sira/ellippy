# Changelog

## 1.2.1

This version corresponds to Ellip v1.2.3.

**Improvements**

- Add reproducible public-Python threshold calibration with independent Rayon and interpreter-detachment controls, branch verification, process-isolated timing, and input-layout validation.
- Own batch dispatch and per-function thresholds in the Python binding, using the published `ellip` kernels and Rayon directly. Calibrate conservative Rayon cutovers on a 12-worker reference host and detach at those cutovers as a responsiveness policy.
- Reject non-contiguous binding inputs with a Python error instead of panicking.

## 1.2.0

**New functions**

- `ellipke(m)`: simultaneous computation of K(m) and E(m).
- `cel3(kc, p)`: complete elliptic integral of the third kind in Bulirsch form.

**Improvements**

- Use upstream Rust-calibrated `ellip-rayon` thresholds.
- Skip GIL release for single-element array calls. `py.detach()` has a fixed overhead that exceeds the cost of the computation itself for small inputs; single-element arrays now bypass it.
- Add `gil_used = false` to `#[pymodule]` for forward compatibility with free-threading Python (PEP 703).
- Add `strip = true` to the release profile to reduce the size of the shared library.

**Dependencies**
- Upgrade ellip from 1.1.3 to 1.2.0 and ellip-rayon from 1.1.3 to 1.2.1. 
- Upgrade PyO3 from 0.26.0 to 0.29.3 and numpy from 0.26.0 to 0.29.0.

## 1.1.3

**Improvements**

- Improve performance by using LTO, opt-level 3, and codegen-units 1.

## 1.1.2

**Improvements**

- Improve performance of `heuman_lambda`.
- Update package metadata.

## 0.1.0

- First release of EllipPy, consistent with ellip v0.5.1.
