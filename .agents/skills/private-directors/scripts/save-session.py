#!/usr/bin/env python3
"""Save a private-directors session result to decisions/results.tsv.

Requires Python 3.9+. No pip install needed — standard library only.

Usage:
    python3 scripts/save-session.py --topic "买房" --score 97 --passed true --iterations 2

Appends one row to decisions/results.tsv (creates file if absent).
"""
from __future__ import annotations

import argparse
import csv
import sys
from datetime import date
from pathlib import Path

RESULTS_TSV = Path(__file__).resolve().parent.parent / "decisions" / "results.tsv"
FIELDS = ["date", "topic", "judge_score", "passed", "iterations", "blocking_items"]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Append session result to results.tsv")
    parser.add_argument("--topic", required=True)
    parser.add_argument("--score", type=float, required=True)
    parser.add_argument("--passed", choices=["true", "false"], required=True)
    parser.add_argument("--iterations", type=int, default=1)
    parser.add_argument("--blocking", default="")
    args = parser.parse_args(argv)

    RESULTS_TSV.parent.mkdir(parents=True, exist_ok=True)
    write_header = not RESULTS_TSV.exists()

    with RESULTS_TSV.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, delimiter="\t")
        if write_header:
            writer.writeheader()
        writer.writerow({
            "date": date.today().isoformat(),
            "topic": args.topic,
            "judge_score": args.score,
            "passed": args.passed,
            "iterations": args.iterations,
            "blocking_items": args.blocking,
        })

    print(f"Saved: {RESULTS_TSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
