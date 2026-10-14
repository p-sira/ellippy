//! First batch sizes using Rayon and interpreter detachment, respectively.
//! Reviewed on a Ryzen 5 4600H with 12 Rayon workers through the public Python
//! API. Conservative Rayon cutovers cover both distributions and GIL contexts.
//! Detach at the same cutover to avoid transitions for small serial calls and
//! allow other Python threads to run during parallel work; this is a
//! responsiveness policy, not a claim that detachment reduces call latency.
//! See benchmarks/perf_calibration/RESULTS.md for evidence and limitations.
//! `usize::MAX` disables an automatic switch.
#![allow(non_upper_case_globals)]

pub(crate) const ellipk: (usize, usize) = (65536, 65536);
pub(crate) const ellipe: (usize, usize) = (32768, 32768);
pub(crate) const ellipf: (usize, usize) = (4096, 4096);
pub(crate) const ellipeinc: (usize, usize) = (2048, 2048);
pub(crate) const ellippi: (usize, usize) = (2048, 2048);
pub(crate) const ellippiinc: (usize, usize) = (1024, 1024);
pub(crate) const ellippiinc_bulirsch: (usize, usize) = (2048, 2048);
pub(crate) const ellipd: (usize, usize) = (8192, 8192);
pub(crate) const ellipdinc: (usize, usize) = (2048, 2048);
pub(crate) const ellipke: (usize, usize) = (32768, 32768);
pub(crate) const cel: (usize, usize) = (32768, 32768);
pub(crate) const cel1: (usize, usize) = (65536, 65536);
pub(crate) const cel2: (usize, usize) = (65536, 65536);
pub(crate) const cel3: (usize, usize) = (32768, 32768);
pub(crate) const el1: (usize, usize) = (16384, 16384);
pub(crate) const el2: (usize, usize) = (4096, 4096);
pub(crate) const el3: (usize, usize) = (4096, 4096);
pub(crate) const elliprf: (usize, usize) = (8192, 8192);
pub(crate) const elliprg: (usize, usize) = (4096, 4096);
pub(crate) const elliprj: (usize, usize) = (4096, 4096);
pub(crate) const elliprc: (usize, usize) = (32768, 32768);
pub(crate) const elliprd: (usize, usize) = (4096, 4096);
pub(crate) const jacobi_zeta: (usize, usize) = (1024, 1024);
pub(crate) const heuman_lambda: (usize, usize) = (1024, 1024);
