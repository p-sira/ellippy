// Threshold discovery binary for cel3 and ellipke Rayon crossover.
// Run: cargo run --bin bench_threshold --release
//
// Measures two families per function:
//   pure Rust  – sequential vs parallel collect only
//   FFI-sim    – same + ffi_copy() to model PyArray1::from_vec O(n) memcopy
//
// Prints side-by-side tables and reports separate suggested thresholds.

use std::time::Instant;

const ITERS: usize = 500;

// ---------------------------------------------------------------------------
// FFI simulator
// ---------------------------------------------------------------------------

/// Simulates the `PyArray1::from_vec` path: allocates a new buffer and copies.
/// Using `std::hint::black_box` prevents the optimizer from eliding the copy.
#[inline(never)]
fn ffi_copy<T: Clone>(v: Vec<T>) -> Vec<T> {
    let mut out = Vec::with_capacity(v.len());
    out.extend_from_slice(&v);
    std::hint::black_box(out)
}

/// Variant for (Vec<f64>, Vec<f64>) tuple returns (ellipke path).
#[inline(never)]
fn ffi_copy2(v: Vec<(f64, f64)>) -> (Vec<f64>, Vec<f64>) {
    let (ks, es): (Vec<f64>, Vec<f64>) = v.into_iter().unzip();
    let ks = std::hint::black_box(ks);
    let es = std::hint::black_box(es);
    (ks, es)
}

// ---------------------------------------------------------------------------
// cel3 – pure Rust
// ---------------------------------------------------------------------------

fn bench_seq_cel3(n: usize) -> f64 {
    let kcs: Vec<f64> = (0..n).map(|i| 0.01 + 0.98 * i as f64 / n as f64).collect();
    let kcs: Vec<f64> = kcs.iter().map(|&m| (1.0 - m).sqrt()).collect();
    let ps: Vec<f64> = vec![0.5; n];

    for _ in 0..20 {
        let _: Result<Vec<f64>, _> = kcs.iter().zip(ps.iter())
            .map(|(&kc, &p)| ellip::cel3(kc, p))
            .collect();
    }

    let t0 = Instant::now();
    for _ in 0..ITERS {
        let _: Result<Vec<f64>, _> = kcs.iter().zip(ps.iter())
            .map(|(&kc, &p)| ellip::cel3(kc, p))
            .collect();
    }
    t0.elapsed().as_nanos() as f64 / ITERS as f64
}

fn bench_par_cel3(n: usize) -> f64 {
    use rayon::prelude::*;
    let kcs: Vec<f64> = (0..n).map(|i| 0.01 + 0.98 * i as f64 / n as f64).collect();
    let kcs: Vec<f64> = kcs.iter().map(|&m| (1.0 - m).sqrt()).collect();
    let ps: Vec<f64> = vec![0.5; n];

    for _ in 0..20 {
        let _: Result<Vec<f64>, _> = kcs.par_iter().zip(ps.par_iter())
            .map(|(&kc, &p)| ellip::cel3(kc, p))
            .collect();
    }

    let t0 = Instant::now();
    for _ in 0..ITERS {
        let _: Result<Vec<f64>, _> = kcs.par_iter().zip(ps.par_iter())
            .map(|(&kc, &p)| ellip::cel3(kc, p))
            .collect();
    }
    t0.elapsed().as_nanos() as f64 / ITERS as f64
}

// ---------------------------------------------------------------------------
// cel3 – FFI-simulated
// ---------------------------------------------------------------------------

fn bench_seq_cel3_ffi(n: usize) -> f64 {
    let kcs: Vec<f64> = (0..n).map(|i| 0.01 + 0.98 * i as f64 / n as f64).collect();
    let kcs: Vec<f64> = kcs.iter().map(|&m| (1.0 - m).sqrt()).collect();
    let ps: Vec<f64> = vec![0.5; n];

    for _ in 0..20 {
        let v: Result<Vec<f64>, _> = kcs.iter().zip(ps.iter())
            .map(|(&kc, &p)| ellip::cel3(kc, p))
            .collect();
        let _ = ffi_copy(v.unwrap());
    }

    let t0 = Instant::now();
    for _ in 0..ITERS {
        let v: Result<Vec<f64>, _> = kcs.iter().zip(ps.iter())
            .map(|(&kc, &p)| ellip::cel3(kc, p))
            .collect();
        let _ = ffi_copy(v.unwrap());
    }
    t0.elapsed().as_nanos() as f64 / ITERS as f64
}

fn bench_par_cel3_ffi(n: usize) -> f64 {
    use rayon::prelude::*;
    let kcs: Vec<f64> = (0..n).map(|i| 0.01 + 0.98 * i as f64 / n as f64).collect();
    let kcs: Vec<f64> = kcs.iter().map(|&m| (1.0 - m).sqrt()).collect();
    let ps: Vec<f64> = vec![0.5; n];

    for _ in 0..20 {
        let v: Result<Vec<f64>, _> = kcs.par_iter().zip(ps.par_iter())
            .map(|(&kc, &p)| ellip::cel3(kc, p))
            .collect();
        let _ = ffi_copy(v.unwrap());
    }

    let t0 = Instant::now();
    for _ in 0..ITERS {
        let v: Result<Vec<f64>, _> = kcs.par_iter().zip(ps.par_iter())
            .map(|(&kc, &p)| ellip::cel3(kc, p))
            .collect();
        let _ = ffi_copy(v.unwrap());
    }
    t0.elapsed().as_nanos() as f64 / ITERS as f64
}

// ---------------------------------------------------------------------------
// ellipke – pure Rust
// ---------------------------------------------------------------------------

fn bench_seq_ke(n: usize) -> f64 {
    let ms: Vec<f64> = (0..n).map(|i| 0.01 + 0.98 * i as f64 / n as f64).collect();

    for _ in 0..20 {
        let _: Result<Vec<(f64, f64)>, _> = ms.iter().map(|&m| ellip::ellipke(m)).collect();
    }

    let t0 = Instant::now();
    for _ in 0..ITERS {
        let _: Result<Vec<(f64, f64)>, _> = ms.iter().map(|&m| ellip::ellipke(m)).collect();
    }
    t0.elapsed().as_nanos() as f64 / ITERS as f64
}

fn bench_par_ke(n: usize) -> f64 {
    use rayon::prelude::*;
    let ms: Vec<f64> = (0..n).map(|i| 0.01 + 0.98 * i as f64 / n as f64).collect();

    for _ in 0..20 {
        let _: Result<Vec<(f64, f64)>, _> = ms.par_iter().map(|&m| ellip::ellipke(m)).collect();
    }

    let t0 = Instant::now();
    for _ in 0..ITERS {
        let _: Result<Vec<(f64, f64)>, _> = ms.par_iter().map(|&m| ellip::ellipke(m)).collect();
    }
    t0.elapsed().as_nanos() as f64 / ITERS as f64
}

// ---------------------------------------------------------------------------
// ellipke – FFI-simulated
// ellipke returns two PyArray1s (K, E) so we simulate two ffi_copy calls.
// ---------------------------------------------------------------------------

fn bench_seq_ke_ffi(n: usize) -> f64 {
    let ms: Vec<f64> = (0..n).map(|i| 0.01 + 0.98 * i as f64 / n as f64).collect();

    for _ in 0..20 {
        let v: Result<Vec<(f64, f64)>, _> = ms.iter().map(|&m| ellip::ellipke(m)).collect();
        let _ = ffi_copy2(v.unwrap());
    }

    let t0 = Instant::now();
    for _ in 0..ITERS {
        let v: Result<Vec<(f64, f64)>, _> = ms.iter().map(|&m| ellip::ellipke(m)).collect();
        let _ = ffi_copy2(v.unwrap());
    }
    t0.elapsed().as_nanos() as f64 / ITERS as f64
}

fn bench_par_ke_ffi(n: usize) -> f64 {
    use rayon::prelude::*;
    let ms: Vec<f64> = (0..n).map(|i| 0.01 + 0.98 * i as f64 / n as f64).collect();

    for _ in 0..20 {
        let v: Result<Vec<(f64, f64)>, _> = ms.par_iter().map(|&m| ellip::ellipke(m)).collect();
        let _ = ffi_copy2(v.unwrap());
    }

    let t0 = Instant::now();
    for _ in 0..ITERS {
        let v: Result<Vec<(f64, f64)>, _> = ms.par_iter().map(|&m| ellip::ellipke(m)).collect();
        let _ = ffi_copy2(v.unwrap());
    }
    t0.elapsed().as_nanos() as f64 / ITERS as f64
}

// ---------------------------------------------------------------------------
// Reporting helpers
// ---------------------------------------------------------------------------

fn print_table_header(title: &str) {
    println!();
    println!("=== {} ===", title);
    println!("{:>7}  {:>12}  {:>12}  {:>9}  winner", "n", "seq ns", "par ns", "ratio");
    println!("{}", "-".repeat(60));
}

fn run_sweep<F, G>(
    sizes: &[usize],
    seq_fn: F,
    par_fn: G,
) -> Option<usize>
where
    F: Fn(usize) -> f64,
    G: Fn(usize) -> f64,
{
    let mut threshold = None;
    for &n in sizes {
        let seq = seq_fn(n);
        let par = par_fn(n);
        let ratio = par / seq;
        let winner = if par < seq { "PAR ✓" } else { "seq" };
        if par < seq && threshold.is_none() {
            threshold = Some(n);
        }
        println!("{:>7}  {:>12.0}  {:>12.0}  {:>9.3}  {}", n, seq, par, ratio, winner);
    }
    threshold
}

// ---------------------------------------------------------------------------
// main
// ---------------------------------------------------------------------------

fn main() {
    let sizes = [
        50, 100, 200, 300, 400, 500, 600, 700, 800, 900,
        1000, 1200, 1500, 2000, 3000, 4000, 5000, 8000, 10000,
        15000, 20000, 30000, 50000,
    ];

    // --- cel3 ---------------------------------------------------------------
    print_table_header("cel3: seq vs par — pure Rust");
    let cel3_rust = run_sweep(&sizes, bench_seq_cel3, bench_par_cel3);

    print_table_header("cel3: seq vs par — FFI-simulated");
    let cel3_ffi = run_sweep(&sizes, bench_seq_cel3_ffi, bench_par_cel3_ffi);

    // --- ellipke ------------------------------------------------------------
    print_table_header("ellipke: seq vs par — pure Rust");
    let ke_rust = run_sweep(&sizes, bench_seq_ke, bench_par_ke);

    print_table_header("ellipke: seq vs par — FFI-simulated");
    let ke_ffi = run_sweep(&sizes, bench_seq_ke_ffi, bench_par_ke_ffi);

    // --- Summary ------------------------------------------------------------
    println!();
    println!("{}", "=".repeat(60));
    println!("SUMMARY");
    println!("{}", "=".repeat(60));

    fn fmt_threshold(t: Option<usize>, label: &str) -> String {
        match t {
            Some(v) => format!("≈ {v}"),
            None => format!("parallel never won in tested range — raise sweep ({label})"),
        }
    }

    println!(
        "cel3    RUST threshold  {}",
        fmt_threshold(cel3_rust, "rust")
    );
    println!(
        "cel3    FFI  threshold  {}",
        fmt_threshold(cel3_ffi, "ffi")
    );
    println!(
        "ellipke RUST threshold  {}",
        fmt_threshold(ke_rust, "rust")
    );
    println!(
        "ellipke FFI  threshold  {}",
        fmt_threshold(ke_ffi, "ffi")
    );

    println!();
    println!("Decision guide:");
    println!("  If FFI threshold >> RUST threshold (> ~20%): add per-function override in lib.rs.");
    println!("  If FFI threshold ≈  RUST threshold (≤ ~20%): ellip-rayon built-ins are sufficient.");
}
