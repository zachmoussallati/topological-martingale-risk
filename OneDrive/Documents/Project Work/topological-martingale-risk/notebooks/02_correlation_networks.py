import os, pandas as pd, networkx as nx, matplotlib.pyplot as plt

os.makedirs("results/plots", exist_ok=True)

returns = pd.read_csv("results/summaries/returns.csv", index_col=0, parse_dates=True)
corr = returns.corr()

G = nx.Graph()
for i in corr.columns:
    for j in corr.columns:
        if i != j:
            G.add_edge(i, j, weight=1 - corr.loc[i, j])

mst = nx.minimum_spanning_tree(G)
plt.figure(figsize=(6, 6))
nx.draw_networkx(mst, with_labels=True, node_color="lightblue")
plt.savefig("results/plots/mst.png")
print("✅ Saved MST plot")
