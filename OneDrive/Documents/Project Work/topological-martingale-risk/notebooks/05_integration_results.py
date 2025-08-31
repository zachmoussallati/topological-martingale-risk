import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from gtda.homology import VietorisRipsPersistence

# Ensure output directories exist
os.makedirs("results/plots", exist_ok=True)
os.makedirs("results/summaries", exist_ok=True)

# Load returns
returns = pd.read_csv("results/summaries/returns.csv", index_col=0, parse_dates=True)

# Rolling window parameters
window = 60  # days
topo_feature_list = []
pricing_error_list = []

# Vietoris-Rips persistence setup
vr = VietorisRipsPersistence(metric='precomputed', homology_dimensions=[0, 1])

# Monte Carlo parameters
n_sim = 1000

for start in range(0, len(returns) - window + 1):
    window_returns = returns.iloc[start:start + window]

    # --- Step 1: Correlation distance & topology ---
    corr = window_returns.corr().values
    dist = np.sqrt(2 * (1 - corr))
    dist_3d = dist[np.newaxis, :, :]
    dgms = vr.fit_transform(dist_3d)

    # --- Step 2: H1 total persistence ---
    h1_total = 0
    if len(dgms[0]) > 1 and dgms[0][1].size > 0:
        intervals = dgms[0][1]
        if intervals.ndim == 1:
            intervals = intervals.reshape(1, -1)
        lifetimes = intervals[:, 1] - intervals[:, 0]
        h1_total = lifetimes.sum()
    topo_feature_list.append(h1_total)

    # --- Step 3: Monte Carlo pricing for this window ---
    np.random.seed(42)  # reproducible
    S0 = window_returns.mean().mean()  # approximate starting price
    mu = 0
    sigma = window_returns.std().mean()
    n_steps = window
    dt = 1 / n_steps

    sims = np.zeros((n_sim, n_steps))
    sims[:, 0] = S0
    for t in range(1, n_steps):
        sims[:, t] = sims[:, t-1] * np.exp((mu - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*np.random.randn(n_sim))

    mc_price = sims[:, -1].mean()
    pricing_error = np.abs(mc_price - window_returns.mean().mean())
    pricing_error_list.append(pricing_error)

# --- Step 4: Save integration results ---
integration_df = pd.DataFrame({
    "H1_TotalPersistence": topo_feature_list,
    "PricingError": pricing_error_list
})
integration_df.to_csv("results/summaries/integration.csv", index=False)

# --- Step 5: Scatter plot ---
plt.figure(figsize=(6, 4))
plt.scatter(topo_feature_list, pricing_error_list, alpha=0.7)
plt.xlabel("H1 Total Persistence")
plt.ylabel("Mean Pricing Error")
plt.title("Topology vs Martingale Pricing Error (Rolling Window)")
plt.tight_layout()
plt.savefig("results/plots/h1_total_vs_price.png")
plt.close()

print("✅ Integrated topology (H1 total persistence) with rolling Monte Carlo pricing and saved scatter plot")
