import os
import numpy as np
import pandas as pd
from gtda.homology import VietorisRipsPersistence
import matplotlib.pyplot as plt

# Ensure output directories exist
os.makedirs("results/plots", exist_ok=True)
os.makedirs("results/summaries", exist_ok=True)

# Load returns from previous step
returns = pd.read_csv("results/summaries/returns.csv", index_col=0, parse_dates=True)

# Compute correlation distance matrix
corr = returns.corr().values
dist = np.sqrt(2 * (1 - corr))  # Convert correlation to distance

# Vietoris-Rips persistence
vr = VietorisRipsPersistence(metric='precomputed', homology_dimensions=[0, 1])
# Fit expects shape (n_samples, n_points, n_features)
dist_3d = dist[np.newaxis, :, :]
dgms = vr.fit_transform(dist_3d)  # dgms is a list/array of persistence diagrams

# Save persistence diagrams safely
np.save("results/summaries/persistence.npy", dgms, allow_pickle=True)

# Optional: plot persistence histogram robustly
plt.figure(figsize=(6, 4))
for dim in [0, 1]:
    all_intervals = []
    for dg in dgms:
        if len(dg) > dim and dg[dim].size > 0:  # check dimension exists and not empty
            intervals = dg[dim]
            if intervals.ndim == 1:  # single feature, make it 2D
                intervals = intervals.reshape(1, -1)
            all_intervals.append(intervals[:, 1] - intervals[:, 0])
    if all_intervals:
        plt.hist(np.hstack(all_intervals), bins=20, alpha=0.5, label=f'H{dim}')
plt.xlabel("Persistence")
plt.ylabel("Count")
plt.title("Persistence Histogram")
plt.legend()
plt.tight_layout()
plt.savefig("results/plots/persistence.png")
plt.close()

print("✅ Saved persistence diagrams and histogram plot")
