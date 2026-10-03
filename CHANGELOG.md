# Changelog

## 1.2.1

**Improvements**

- Upgrade PyO3 from 0.26.0 to 0.29.3 and numpy from 0.26.0 to 0.29.0.
- Skip GIL release for single-element array calls. `py.detach()` has a fixed overhead that exceeds the cost of the computation itself for small inputs; single-element arrays now bypass it.
- Add `gil_used = false` to `#[pymodule]` for forward compatibility with free-threading Python (PEP 703).
- Add `strip = true` to the release profile to reduce the size of the shared library.

## 1.2.0

**New functions**

- `ellipke(m)`: simultaneous computation of K(m) and E(m).
- `cel3(kc, p)`: complete elliptic integral of the third kind in Bulirsch form.

## 1.1.3

**Improvements**

- Improve performance by using LTO, opt-level 3, and codegen-units 1.

## 1.1.2

**Improvements**

- Improve performance of `heuman_lambda`.
- Update package metadata.

## 0.1.0

- First release of EllipPy, consistent with ellip v0.5.1.
