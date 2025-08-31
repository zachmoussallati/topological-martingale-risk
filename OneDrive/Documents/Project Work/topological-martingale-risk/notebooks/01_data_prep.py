import argparse
import os
import pandas as pd
import yfinance as yf

# Ensure output directories exist
os.makedirs("results/summaries", exist_ok=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download stock data and compute returns")
    parser.add_argument("--tickers", nargs="+", required=True, help="List of stock tickers")
    parser.add_argument("--start", required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", required=True, help="End date (YYYY-MM-DD)")
    args = parser.parse_args()

    # Download adjusted close prices
    data = yf.download(
        args.tickers,
        start=args.start,
        end=args.end,
        group_by='ticker',
        auto_adjust=True  # fixes the FutureWarning and returns adjusted prices
    )

    # Handle multiple tickers (MultiIndex columns)
    if isinstance(data.columns, pd.MultiIndex):
        adj_close = pd.concat([data[ticker]['Close'] for ticker in args.tickers], axis=1)
        adj_close.columns = args.tickers
    else:
        adj_close = data  # single ticker case

    # Save prices
    adj_close.to_csv("results/summaries/prices.csv")

    # Compute daily returns
    returns = adj_close.pct_change().dropna()
    returns.to_csv("results/summaries/returns.csv")

    print("✅ Saved prices and returns")

