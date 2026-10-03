/*
 * EllipPy is licensed under The 3-Clause BSD, see LICENSE.
 * Copyright 2025 Sira Pornsiriprasert <code@psira.me>
 */

use numpy::{PyArray1, PyReadonlyArray1};
use pyo3::{exceptions::PyRuntimeError, prelude::*};
use rayon::prelude::*;

macro_rules! impl_py {
    ($($func:ident : $scalar_func:ident : [$($args:ident),+] : $n_args:tt),* ; $($extra:ident),* $(,)?) => {
        $(
            #[pyfunction]
            pub fn $func<'py>(
                py: Python<'py>,
                $($args: PyReadonlyArray1<f64>),*
            ) -> PyResult<Bound<'py, PyArray1<f64>>> {
                $(
                    let $args = $args.as_slice().expect("Non-contiguous array");
                )*
                let result = py.detach(|| ellip_rayon::$func($($args),*));
                match result {
                    Ok(ans) => Ok(PyArray1::from_vec(py, ans)),
                    Err(e) => Err(PyRuntimeError::new_err(e)),
                }
            }

            #[pyfunction]
            pub fn $scalar_func(
                $($args: f64),*
            ) -> PyResult<f64> {
                match ellip::$func($($args),*) {
                    Ok(ans) => Ok(ans),
                    Err(e) => Err(PyRuntimeError::new_err(e)),
                }
            }
        )*

        #[pymodule]
        #[pyo3(name="ellippy_binding")]
        fn ellippy_binding(m: &Bound<'_, PyModule>) -> PyResult<()> {
            $(
                m.add_function(wrap_pyfunction!($func, m)?)?;
                m.add_function(wrap_pyfunction!($scalar_func, m)?)?;
            )*
            $(
                m.add_function(wrap_pyfunction!($extra, m)?)?;
            )*
            Ok(())
        }

    };
}

// `cel3` and `ellipke` are provided by ellip 1.2.0 but are not exposed by
// ellip-rayon 1.2.0. Their array bindings are therefore implemented here,
// mirroring the parallelization strategy used by the `impl_py!` macro.

#[pyfunction]
pub fn cel3<'py>(
    py: Python<'py>,
    kc: PyReadonlyArray1<f64>,
    p: PyReadonlyArray1<f64>,
) -> PyResult<Bound<'py, PyArray1<f64>>> {
    let kc = kc.as_slice().expect("Non-contiguous array");
    let p = p.as_slice().expect("Non-contiguous array");
    if kc.len() != p.len() {
        return Err(PyRuntimeError::new_err(
            "cel3: All arguments must have the same length.",
        ));
    }
    const THRESHOLD: usize = 600;
    let result = py.detach(|| {
        if kc.len() < THRESHOLD {
            kc.iter()
                .zip(p.iter())
                .map(|(&kc, &p)| ellip::cel3(kc, p))
                .collect::<Result<Vec<f64>, _>>()
        } else {
            kc.par_iter()
                .zip(p.par_iter())
                .map(|(&kc, &p)| ellip::cel3(kc, p))
                .collect::<Result<Vec<f64>, _>>()
        }
    });
    match result {
        Ok(ans) => Ok(PyArray1::from_vec(py, ans)),
        Err(e) => Err(PyRuntimeError::new_err(e)),
    }
}

#[pyfunction]
pub fn cel3_scalar(kc: f64, p: f64) -> PyResult<f64> {
    match ellip::cel3(kc, p) {
        Ok(ans) => Ok(ans),
        Err(e) => Err(PyRuntimeError::new_err(e)),
    }
}

#[pyfunction]
pub fn ellipke<'py>(
    py: Python<'py>,
    m: PyReadonlyArray1<f64>,
) -> PyResult<(Bound<'py, PyArray1<f64>>, Bound<'py, PyArray1<f64>>)> {
    let m = m.as_slice().expect("Non-contiguous array");
    const THRESHOLD: usize = 1000;
    let result = py.detach(|| {
        if m.len() < THRESHOLD {
            m.iter()
                .map(|&m| ellip::ellipke(m))
                .collect::<Result<Vec<(f64, f64)>, _>>()
        } else {
            m.par_iter()
                .map(|&m| ellip::ellipke(m))
                .collect::<Result<Vec<(f64, f64)>, _>>()
        }
    });
    match result {
        Ok(ans) => {
            let (ks, es): (Vec<f64>, Vec<f64>) = ans.into_iter().unzip();
            Ok((PyArray1::from_vec(py, ks), PyArray1::from_vec(py, es)))
        }
        Err(e) => Err(PyRuntimeError::new_err(e)),
    }
}

#[pyfunction]
pub fn ellipke_scalar(m: f64) -> PyResult<(f64, f64)> {
    match ellip::ellipke(m) {
        Ok(ans) => Ok(ans),
        Err(e) => Err(PyRuntimeError::new_err(e)),
    }
}

impl_py!(
    ellipk:ellipk_scalar:[m]:1,
    ellipe:ellipe_scalar:[m]:1,
    ellipf:ellipf_scalar:[phi, m]:2,
    ellipeinc:ellipeinc_scalar:[phi, m]:2,
    ellippi:ellippi_scalar:[n, m]:2,
    ellippiinc:ellippiinc_scalar:[phi, n, m]:3,
    ellippiinc_bulirsch:ellippiinc_bulirsch_scalar:[phi, n, m]:3,
    ellipd:ellipd_scalar:[m]:1,
    ellipdinc:ellipdinc_scalar:[phi, m]:2,
    cel:cel_scalar:[kc, p, a, b]:4,
    cel1:cel1_scalar:[kc]:1,
    cel2:cel2_scalar:[kc, a, b]:3,
    el1:el1_scalar:[x, kc]:2,
    el2:el2_scalar:[x, kc, a, b]:4,
    el3:el3_scalar:[x, kc, p]:3,
    elliprf:elliprf_scalar:[x, y, z]:3,
    elliprg:elliprg_scalar:[x, y, z]:3,
    elliprj:elliprj_scalar:[x, y, z, p]:4,
    elliprc:elliprc_scalar:[x, y]:2,
    elliprd:elliprd_scalar:[x, y, z]:3,
    jacobi_zeta:jacobi_zeta_scalar:[phi, m]:2,
    heuman_lambda:heuman_lambda_scalar:[phi, m]:2;
    cel3, cel3_scalar, ellipke, ellipke_scalar
);
