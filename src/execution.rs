//! Overrides and counters exist only in explicit calibration builds.

#[cfg(not(feature = "threshold-calibration"))]
#[inline]
pub(crate) const fn should_parallel(auto: bool) -> bool {
    auto
}
#[cfg(not(feature = "threshold-calibration"))]
#[inline]
pub(crate) const fn should_detach(auto: bool) -> bool {
    auto
}

#[cfg(feature = "threshold-calibration")]
mod calibration {
    use pyo3::{exceptions::PyValueError, prelude::*, types::PyDict};
    use std::sync::atomic::{AtomicBool, AtomicU8, AtomicU64, Ordering::Relaxed};

    static RUST_MODE: AtomicU8 = AtomicU8::new(0);
    static GIL_MODE: AtomicU8 = AtomicU8::new(0);
    static INSTRUMENT: AtomicBool = AtomicBool::new(false);
    static COUNTS: [AtomicU64; 4] = [const { AtomicU64::new(0) }; 4];

    fn choose(auto: bool, mode: &AtomicU8, offset: usize) -> bool {
        let chosen = match mode.load(Relaxed) {
            1 => false,
            2 => true,
            _ => auto,
        };
        if INSTRUMENT.load(Relaxed) {
            COUNTS[offset + usize::from(chosen)].fetch_add(1, Relaxed);
        }
        chosen
    }
    pub(crate) fn should_parallel(auto: bool) -> bool {
        choose(auto, &RUST_MODE, 0)
    }
    pub(crate) fn should_detach(auto: bool) -> bool {
        choose(auto, &GIL_MODE, 2)
    }

    #[pyfunction]
    #[pyo3(signature = (rust_mode="auto", gil_mode="auto", instrument=false))]
    pub(crate) fn _set_threshold_calibration(
        rust_mode: &str,
        gil_mode: &str,
        instrument: bool,
    ) -> PyResult<()> {
        let parse = |value, names: [&str; 3]| {
            names
                .iter()
                .position(|&name| name == value)
                .map(|i| i as u8)
                .ok_or_else(|| {
                    PyValueError::new_err(format!("Invalid mode {value:?}; expected {names:?}"))
                })
        };
        // Validate both before changing global state. Workers must be isolated.
        let rust = parse(rust_mode, ["auto", "serial", "parallel"])?;
        let gil = parse(gil_mode, ["auto", "retain", "detach"])?;
        RUST_MODE.store(rust, Relaxed);
        GIL_MODE.store(gil, Relaxed);
        INSTRUMENT.store(instrument, Relaxed);
        for count in &COUNTS {
            count.store(0, Relaxed);
        }
        Ok(())
    }

    #[pyfunction]
    pub(crate) fn _threshold_calibration_state(py: Python<'_>) -> PyResult<Bound<'_, PyDict>> {
        let state = PyDict::new(py);
        state.set_item(
            "rust_mode",
            ["auto", "serial", "parallel"][RUST_MODE.load(Relaxed) as usize],
        )?;
        state.set_item(
            "gil_mode",
            ["auto", "retain", "detach"][GIL_MODE.load(Relaxed) as usize],
        )?;
        state.set_item("instrument", INSTRUMENT.load(Relaxed))?;
        state.set_item(
            "rust_branches",
            (COUNTS[0].load(Relaxed), COUNTS[1].load(Relaxed)),
        )?;
        state.set_item(
            "gil_branches",
            (COUNTS[2].load(Relaxed), COUNTS[3].load(Relaxed)),
        )?;
        state.set_item("rayon_threads", rayon::current_num_threads())?;
        let thresholds = PyDict::new(py);
        // Read the exact constants compiled into this extension.
        macro_rules! add { ($($name:ident),+) => { $(thresholds.set_item(stringify!($name), crate::thresholds::$name)?;)+ }; }
        add!(
            ellipk,
            ellipe,
            ellipke,
            ellipf,
            ellipeinc,
            ellippi,
            ellippiinc,
            ellippiinc_bulirsch,
            ellipd,
            ellipdinc,
            cel,
            cel1,
            cel2,
            cel3,
            el1,
            el2,
            el3,
            elliprf,
            elliprg,
            elliprj,
            elliprc,
            elliprd,
            jacobi_zeta,
            heuman_lambda
        );
        state.set_item("thresholds", thresholds)?;
        Ok(state)
    }
}
#[cfg(feature = "threshold-calibration")]
pub(crate) use calibration::*;
