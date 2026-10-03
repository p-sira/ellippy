/*
 * EllipPy is licensed under The 3-Clause BSD, see LICENSE.
 * Copyright 2025 Sira Pornsiriprasert <code@psira.me>
 */

use numpy::{PyArray1, PyReadonlyArray1};
use pyo3::{exceptions::PyRuntimeError, prelude::*};

/// Release the GIL only when it is worth it.
///
/// For small batches, the GIL-release/reacquire round-trip plus Rayon
/// scheduling overhead can exceed the computation itself.  We skip
/// `py.detach()` when `$n <= DETACH_THRESHOLD`.
///
/// The threshold of 32 matches pymagba's empirically-determined value for
/// Dipole, whose per-point cost (elliptic integrals) is comparable to ours.
const DETACH_THRESHOLD: usize = 32;

/// FFI-aware parallelism threshold for `cel3`.
///
/// `ellip-rayon`'s internal threshold is calibrated at the pure-Rust level
/// (~8k elements).  The `PyArray1::from_vec` O(n) copy on every return path
/// shifts the actual break-even upward to ~10k elements (+25%).  Because
/// that gap exceeds our 20% tolerance band we override it here: for
/// `n <= CEL3_FFI_THRESHOLD` we call the sequential path directly, bypassing
/// rayon entirely.
///
/// Determined by `cargo run --bin bench_threshold --release`.
const CEL3_FFI_THRESHOLD: usize = 10_000;

macro_rules! detach_if_multi {
    ($py:expr, $n:expr, $work:expr) => {
        if $n <= DETACH_THRESHOLD {
            $work
        } else {
            $py.detach(|| $work)
        }
    };
}

macro_rules! impl_py {
    // -----------------------------------------------------------------------
    // Main arm.
    //
    // Two semicolon-separated sections:
    //
    //   rayon { func:scalar:[args], ... }
    //     Functions in ellip-rayon returning Vec<f64>; parallelism is
    //     delegated to ellip-rayon's internal threshold.
    //
    //   tuple { func:scalar:[args], ... }
    //     Functions in ellip-rayon returning Vec<(f64, f64)>; the result
    //     is unzipped into two PyArray1s.  Currently: ellipke only.
    // -----------------------------------------------------------------------
    (
        $($rfunc:ident : $rscalar:ident : [$($rargs:ident),+]),* $(,)? ;
        $($tfunc:ident : $tscalar:ident : [$($targs:ident),+]),* $(,)?
    ) => {
        // --- Rayon-backed, single Vec<f64> return --------------------------
        $(
            #[pyfunction]
            pub fn $rfunc<'py>(
                py: Python<'py>,
                $($rargs: PyReadonlyArray1<f64>),*
            ) -> PyResult<Bound<'py, PyArray1<f64>>> {
                $( let $rargs = $rargs.as_slice().expect("Non-contiguous array"); )*
                let n = impl_py!(@first_len $($rargs),*);
                let result = detach_if_multi!(py, n, ellip_rayon::$rfunc($($rargs),*));
                match result {
                    Ok(ans) => Ok(PyArray1::from_vec(py, ans)),
                    Err(e) => Err(PyRuntimeError::new_err(e)),
                }
            }

            #[pyfunction]
            pub fn $rscalar($($rargs: f64),*) -> PyResult<f64> {
                match ellip::$rfunc($($rargs),*) {
                    Ok(ans) => Ok(ans),
                    Err(e) => Err(PyRuntimeError::new_err(e)),
                }
            }
        )*

        // --- Rayon-backed, (Vec<f64>, Vec<f64>) tuple return ---------------
        $(
            #[pyfunction]
            pub fn $tfunc<'py>(
                py: Python<'py>,
                $($targs: PyReadonlyArray1<f64>),*
            ) -> PyResult<(Bound<'py, PyArray1<f64>>, Bound<'py, PyArray1<f64>>)> {
                $( let $targs = $targs.as_slice().expect("Non-contiguous array"); )*
                let n = impl_py!(@first_len $($targs),*);
                let result = detach_if_multi!(py, n, ellip_rayon::$tfunc($($targs),*));
                match result {
                    Ok(ans) => {
                        let (ks, es): (Vec<f64>, Vec<f64>) = ans.into_iter().unzip();
                        Ok((PyArray1::from_vec(py, ks), PyArray1::from_vec(py, es)))
                    }
                    Err(e) => Err(PyRuntimeError::new_err(e)),
                }
            }

            #[pyfunction]
            pub fn $tscalar($($targs: f64),*) -> PyResult<(f64, f64)> {
                match ellip::$tfunc($($targs),*) {
                    Ok(ans) => Ok(ans),
                    Err(e) => Err(PyRuntimeError::new_err(e)),
                }
            }
        )*

        #[pymodule(gil_used = false)]
        #[pyo3(name = "ellippy_binding")]
        fn ellippy_binding(m: &Bound<'_, PyModule>) -> PyResult<()> {
            $(
                m.add_function(wrap_pyfunction!($rfunc, m)?)?;
                m.add_function(wrap_pyfunction!($rscalar, m)?)?;
            )*
            $(
                m.add_function(wrap_pyfunction!($tfunc, m)?)?;
                m.add_function(wrap_pyfunction!($tscalar, m)?)?;
            )*
            Ok(())
        }
    };

    // Helper: length of first argument slice.
    (@first_len $head:ident $(, $tail:ident)*) => { $head.len() };
}

// ---------------------------------------------------------------------------
// cel3: hand-written to apply CEL3_FFI_THRESHOLD instead of ellip-rayon's
// internal pure-Rust threshold.
// ---------------------------------------------------------------------------

#[pyfunction]
pub fn cel3<'py>(
    py: Python<'py>,
    kc: PyReadonlyArray1<f64>,
    p: PyReadonlyArray1<f64>,
) -> PyResult<Bound<'py, PyArray1<f64>>> {
    let kc = kc.as_slice().expect("Non-contiguous array");
    let p = p.as_slice().expect("Non-contiguous array");
    let n = kc.len();
    let result = if n <= CEL3_FFI_THRESHOLD {
        // Sequential: rayon overhead + FFI copy not worth it at this size.
        kc.iter()
            .zip(p.iter())
            .map(|(&kc, &p)| ellip::cel3(kc, p))
            .collect::<Result<Vec<f64>, _>>()
            .map_err(PyRuntimeError::new_err)
    } else {
        detach_if_multi!(py, n, ellip_rayon::cel3(kc, p))
            .map_err(PyRuntimeError::new_err)
    };
    result.map(|ans| PyArray1::from_vec(py, ans))
}

#[pyfunction]
pub fn cel3_scalar(kc: f64, p: f64) -> PyResult<f64> {
    match ellip::cel3(kc, p) {
        Ok(ans) => Ok(ans),
        Err(e) => Err(PyRuntimeError::new_err(e)),
    }
}

impl_py!(
    // Rayon-backed, single Vec<f64> return
    ellipk             : ellipk_scalar             : [m],
    ellipe             : ellipe_scalar             : [m],
    ellipf             : ellipf_scalar             : [phi, m],
    ellipeinc          : ellipeinc_scalar          : [phi, m],
    ellippi            : ellippi_scalar            : [n, m],
    ellippiinc         : ellippiinc_scalar         : [phi, n, m],
    ellippiinc_bulirsch: ellippiinc_bulirsch_scalar: [phi, n, m],
    ellipd             : ellipd_scalar             : [m],
    ellipdinc          : ellipdinc_scalar          : [phi, m],
    cel                : cel_scalar                : [kc, p, a, b],
    cel1               : cel1_scalar               : [kc],
    cel2               : cel2_scalar               : [kc, a, b],
    // cel3 is hand-written above (CEL3_FFI_THRESHOLD override)
    el1                : el1_scalar                : [x, kc],
    el2                : el2_scalar                : [x, kc, a, b],
    el3                : el3_scalar                : [x, kc, p],
    elliprf            : elliprf_scalar            : [x, y, z],
    elliprg            : elliprg_scalar            : [x, y, z],
    elliprj            : elliprj_scalar            : [x, y, z, p],
    elliprc            : elliprc_scalar            : [x, y],
    elliprd            : elliprd_scalar            : [x, y, z],
    jacobi_zeta        : jacobi_zeta_scalar        : [phi, m],
    heuman_lambda      : heuman_lambda_scalar      : [phi, m]
    ;
    // Rayon-backed, (Vec<f64>, Vec<f64>) tuple return
    ellipke            : ellipke_scalar            : [m]
);
