/*
 * EllipPy is licensed under The 3-Clause BSD, see LICENSE.
 * Copyright 2025 Sira Pornsiriprasert <code@psira.me>
 */

use numpy::{PyArray1, PyReadonlyArray1};
use pyo3::{exceptions::PyRuntimeError, prelude::*};

use rayon::prelude::*;

mod execution;
mod thresholds;

// Both paths call the same scalar kernel and preserve input order. Keeping
// dispatch here makes thresholds part of the Python wheel's source snapshot.
fn batch<T: Send>(
    n: usize,
    parallel: bool,
    f: impl Fn(usize) -> Result<T, ellip::StrErr> + Sync + Send,
) -> Result<Vec<T>, ellip::StrErr> {
    if parallel {
        (0..n).into_par_iter().map(f).collect()
    } else {
        (0..n).map(f).collect()
    }
}

macro_rules! compute_batch {
    ($py:expr, $func:ident, $n:expr, [$($arg:ident),+]) => {{
        $(if $arg.len() != $n {
            return Err(PyRuntimeError::new_err(concat!(stringify!($func), ": All arguments must have the same length.")));
        })+
        let thresholds = thresholds::$func;
        let parallel = execution::should_parallel($n >= thresholds.0);
        let work = || batch($n, parallel, |i| ellip::$func($($arg[i]),+));
        if execution::should_detach($n >= thresholds.1) {
            $py.detach(work)
        } else {
            work()
        }
    }};
}

macro_rules! impl_py {
    // -----------------------------------------------------------------------
    // Main arm.
    //
    // Two semicolon-separated sections:
    //
    //   rayon { func:scalar:[args], ... }
    //     Batch functions returning Vec<f64>, with binding-owned dispatch.
    //
    //   tuple { func:scalar:[args], ... }
    //     Batch functions returning Vec<(f64, f64)>; the result
    //     is unzipped into two PyArray1s.  Currently: ellipke only.
    // -----------------------------------------------------------------------
    (
        $($rfunc:ident : $rscalar:ident : [$($rargs:ident),+]),* $(,)? ;
        @return_tuple
        $($tfunc:ident : $tscalar:ident : [$($targs:ident),+]),* $(,)?
    ) => {
        // --- Rayon-backed, single Vec<f64> return --------------------------
        $(
            #[pyfunction]
            pub fn $rfunc<'py>(
                py: Python<'py>,
                $($rargs: PyReadonlyArray1<f64>),*
            ) -> PyResult<Bound<'py, PyArray1<f64>>> {
                $( let $rargs = $rargs.as_slice().map_err(|_| pyo3::exceptions::PyValueError::new_err("Expected contiguous arrays"))?; )*
                let n = impl_py!(@first_len $($rargs),*);
                let result = compute_batch!(py, $rfunc, n, [$($rargs),*]);
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
                $( let $targs = $targs.as_slice().map_err(|_| pyo3::exceptions::PyValueError::new_err("Expected contiguous arrays"))?; )*
                let n = impl_py!(@first_len $($targs),*);
                let result = compute_batch!(py, $tfunc, n, [$($targs),*]);
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
            #[cfg(feature = "threshold-calibration")]
            {
                m.add_function(wrap_pyfunction!(execution::_set_threshold_calibration, m)?)?;
                m.add_function(wrap_pyfunction!(execution::_threshold_calibration_state, m)?)?;
            }
            Ok(())
        }
    };

    // Helper: length of first argument slice.
    (@first_len $head:ident $(, $tail:ident)*) => { $head.len() };
}

// Per-function Rayon and interpreter thresholds live in thresholds.rs.
impl_py!(
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
    cel3               : cel3_scalar               : [kc, p],
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
    @return_tuple
    ellipke            : ellipke_scalar            : [m]
);
