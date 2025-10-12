/*
 * EllipPy is licensed under The 3-Clause BSD, see LICENSE.
 * Copyright 2025 Sira Pornsiriprasert <code@psira.me>
 */

use numpy::{PyArray1, PyReadonlyArray1};
use pyo3::{exceptions::PyRuntimeError, prelude::*};

macro_rules! impl_py {
    ($($func:ident : $func_name:literal : [$($args:ident),+] : $n_args:tt),* $(,)?) => {
        $(
            #[pyfunction(name = $func_name)]
            pub fn $func<'py>(
                py: Python<'py>,
                $($args: PyReadonlyArray1<f64>),*
            ) -> PyResult<Bound<'py, PyArray1<f64>>> {
                let result = ellip_rayon::$func($($args.as_slice().expect("Non-contiguous array")),*);
                match result {
                    Ok(ans) => Ok(PyArray1::from_vec(py, ans)),
                    Err(e) => Err(PyRuntimeError::new_err(e)),
                }
            }
        )*

        #[pymodule]
        #[pyo3(name="ellippy_binding")]
        fn ellippy_binding(m: &Bound<'_, PyModule>) -> PyResult<()> {
            $(
                m.add_function(wrap_pyfunction!($func, m)?)?;
            )*
            Ok(())
        }

    };
}

impl_py!(
    ellipk:"ellipk":[m]:1,
    ellipe:"ellipe":[m]:1,
    ellipf:"ellipf":[phi, m]:2,
    ellipeinc:"ellipeinc":[phi, m]:2,
    ellippi:"ellippi":[n, m]:2,
    ellippiinc:"ellippiinc":[phi, n, m]:3,
    ellippiinc_bulirsch:"ellippiinc_bulirsch":[phi, n, m]:3,
    ellipd:"ellipd":[m]:1,
    ellipdinc:"ellipdinc":[phi, m]:2,
    cel:"cel":[kc, p, a, b]:4,
    cel1:"cel1":[kc]:1,
    cel2:"cel2":[kc, a, b]:3,
    el1:"el1":[x, kc]:2,
    el2:"el2":[x, kc, a, b]:4,
    el3:"el3":[x, kc, p]:3,
    elliprf:"elliprf":[x, y, z]:3,
    elliprg:"elliprg":[x, y, z]:3,
    elliprj:"elliprj":[x, y, z, p]:4,
    elliprc:"elliprc":[x, y]:2,
    elliprd:"elliprd":[x, y, z]:3,
    jacobi_zeta:"jacobi_zeta":[phi, m]:2,
    heuman_lambda:"heuman_lambda":[phi, m]:2,
);
