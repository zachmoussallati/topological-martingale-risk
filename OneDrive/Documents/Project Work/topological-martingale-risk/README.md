# Topological Martingale Risk

**Author:** Zacharia Moussallati  
**Date:** 2025-08-31

---

## Overview

This project investigates the relationship between market correlation topology and martingale-based pricing errors using historical stock data. By combining topological data analysis (TDA) with Monte Carlo martingale simulations, we explore whether structural changes in asset correlations can predict deviations in pricing models.  

The pipeline is fully automated, from data acquisition to integration and plotting, and is ready to run for any set of tickers.

---

## Motivation

- Traditional quantitative finance assumes that asset prices follow a martingale process under the risk-neutral measure.  
- Empirically, deviations occur due to complex interdependencies between assets.  
- Topological data analysis (TDA) provides tools to quantify the “shape” of correlations using persistent homology.  
- By integrating persistent homology features with Monte Carlo pricing, we aim to detect periods where market topology indicates higher risk of pricing errors.

---

## Methodology

### 1. Data Acquisition

- Adjusted close prices are downloaded from Yahoo Finance using `yfinance`.  
- Daily log returns are computed for each asset.

### 2. Correlation Networks

- Compute the correlation matrix of asset returns.  
- Convert correlations to a distance metric:

`d_ij = sqrt(2 * (1 - rho_ij))`

where `rho_ij` is the Pearson correlation between assets `i` and `j`.  

- Construct a **Minimum Spanning Tree (MST)** to visualise the correlation network.

### 3. Topological Analysis (TDA)

- Use Vietoris-Rips persistence to compute 0D and 1D homology of the correlation distance matrix.  
- Key features:
  - **H0**: connected components (Betti0)  
  - **H1**: loops (Betti1 / persistence intervals)

- Compute **H1 total persistence**:

`H1 Total Persistence = sum_i (death_i - birth_i)`

This measures the “strength” of loop structures in the correlation network.

### 4. Monte Carlo Martingale Pricing

- For each rolling window of returns:

`S_{t+Δt} = S_t * exp((μ - 0.5*σ^2)*Δt + σ*sqrt(Δt)*Z_t), where Z_t ~ N(0,1)`

where `S_t` is the price, `μ = 0`, and `σ` is estimated from returns.  

- Compute the mean Monte Carlo terminal price and compare it to observed returns.  
- Define **pricing error** as the absolute difference:

`Pricing Error = | MC Price - Observed Mean Price |`

### 5. Integration

- For each rolling window:
  - Compute **H1 total persistence** from topology analysis.  
  - Compute **Monte Carlo pricing error** for the same window.  
- Produce a **scatter plot** of `H1 Total Persistence` vs `Pricing Error`.  
- Save integration results as CSV for further analysis.

---

## Installation

```bash
# Clone repository
git clone https://github.com/zachmoussallati/topological-martingale-risk.git
cd topological-martingale-risk

# Create virtual environment (recommended)
python -m venv .venv

# Activate
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt








