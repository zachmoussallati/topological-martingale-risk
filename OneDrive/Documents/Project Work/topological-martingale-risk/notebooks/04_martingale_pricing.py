import os, numpy as np, pandas as pd

os.makedirs("results/summaries", exist_ok=True)

np.random.seed(42)
returns = pd.read_csv("results/summaries/returns.csv", index_col=0, parse_dates=True)

S0 = 100
mu, sigma = returns.mean().mean(), returns.std().mean()
T, steps, n_paths = 1, 252, 1000

dt = T / steps
paths = np.zeros((steps+1, n_paths))
paths[0] = S0

for t in range(1, steps+1):
    z = np.random.randn(n_paths)
    paths[t] = paths[t-1] * np.exp((mu - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*z)

mc_price = np.mean(np.maximum(paths[-1]-S0, 0)) * np.exp(-mu*T)

pd.DataFrame({"MC_Call": [mc_price]}).to_csv("results/summaries/mc_pricing.csv")
print("✅ Monte Carlo pricing done")
