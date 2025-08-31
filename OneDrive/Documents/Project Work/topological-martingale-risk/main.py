#!/usr/bin/env python3
import subprocess, argparse, sys

# Ordered pipeline scripts
scripts = [
    "notebooks/01_data_prep.py",
    "notebooks/02_correlation_networks.py",
    "notebooks/03_topology_analysis.py",
    "notebooks/04_martingale_pricing.py",
    "notebooks/05_integration_results.py",
]

def main():
    p = argparse.ArgumentParser(
        description="Run full Topological Martingale Risk pipeline."
    )
    p.add_argument("--tickers", nargs="+", required=True, help="List of stock tickers")
    p.add_argument("--start", required=True, help="Start date (YYYY-MM-DD)")
    p.add_argument("--end", required=True, help="End date (YYYY-MM-DD)")
    args = p.parse_args()

    # Run the first script (data prep) with CLI args
    print(f"[INFO] Running {scripts[0]} with tickers {args.tickers}")
    subprocess.run(
        ["python", scripts[0], "--tickers", *args.tickers, "--start", args.start, "--end", args.end],
        check=True
    )

    # Run the rest in order
    for s in scripts[1:]:
        print(f"[INFO] Running {s}")
        subprocess.run(["python", s], check=True)

if __name__ == "__main__":
    sys.exit(main())
