# Topological Martingale Risk

**Author:** Zacharia Moussallati  
**Date:** 2025-08-31  

---

## Description

This repository contains a project investigating the relationship between **market correlation topology** and **martingale-based pricing errors** using historical stock data. The analysis combines **topological data analysis (TDA)** with **Monte Carlo martingale simulations** to explore whether structural changes in asset correlations can predict deviations in pricing models.

For full details, methodology, derivations, and results, please refer to the main Jupyter notebook:
[**Topological_Martingale_Risk.ipynb**]

---

## Usage

1. Open `Topological_Martingale_Risk.ipynb` in Jupyter Notebook or Jupyter Lab.  
2. Follow the instructions in the notebook to run the full analysis.

---

## Repository Structure

```text
topological-martingale-risk/
├── Topological_Martingale_Risk.ipynb   # Main notebook with full analysis
├── main.py                             # Python orchestrator for pipeline
├── requirements.txt                    # Python dependencies
├── README.md                            # This file
├── notebooks/                           # Scripts for each step of the pipeline
│   ├── 01_data_prep.py
│   ├── 02_correlation_networks.py
│   ├── 03_topology_analysis.py
│   ├── 04_martingale_pricing.py
│   └── 05_integration_results.py
└── results/                             # Generated outputs
    ├── summaries/                       # CSVs of prices, returns, persistence, MC pricing, integration
    └── plots/                           # MST plots, persistence histograms, Betti vs Price scatter


