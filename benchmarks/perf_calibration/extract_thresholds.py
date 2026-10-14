#!/usr/bin/env python3
# EllipPy is licensed under The 3-Clause BSD; see LICENSE.
"""Summarize a single calibration run; candidates require review before use."""

import argparse
import json
from pathlib import Path


def render(report):
    lines = [
        "# Python-path calibration candidates",
        "",
        "Values are first switch sizes (`n >= threshold`). No crossover is not a threshold.",
        "",
        "| Function | Layout | Distribution | Decision | Status | First size | Candidate range |",
        "|---|---|---|---|---|---:|---|",
    ]
    for row in report["candidates"]:
        bounds = row["candidate_range"]
        lines.append(
            f"| {row['case']} | {row['layout']} | {row['distribution']} | {row['comparison']} | {row['status']} | {row['first_switch_size'] or '—'} | {str(bounds) if bounds else '—'} |"
        )
    return "\n".join(lines) + "\n"


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("report", type=Path)
    p.add_argument("--output", type=Path)
    args = p.parse_args()
    report = json.loads(args.report.read_text())
    if report.get("schema") != 1 or not report.get("candidates"):
        raise SystemExit("Not a completed EllipPy calibration report")
    text = render(report)
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
