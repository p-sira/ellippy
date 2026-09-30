/*
 * EllipPy is licensed under The 3-Clause BSD, see LICENSE.
 * Copyright 2025 Sira Pornsiriprasert <code@psira.me>
 */

use numpy::{PyArray1, PyReadonlyArray1};
use pyo3::{exceptions::PyRuntimeError, prelude::*};

macro_rules! impl_py {
    ($($func:ident : $scalar_func:ident : [$($args:ident),+] : $n_args:tt),* $(,)?) => {
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
            Ok(())
        }

    };
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
    heuman_lambda:heuman_lambda_scalar:[phi, m]:2,
);
