# Topological Martingale Risk

**Author:** Zacharia Moussallati  
**Date:** 2025-08-31

---

## Overview

This project investigates the relationship between **market correlation topology** and **martingale-based pricing errors** using historical stock data. By combining **topological data analysis (TDA)** with **Monte Carlo martingale simulations**, we explore whether structural changes in asset correlations can predict deviations in pricing models.  

The pipeline is fully automated, from data acquisition to integration and plotting, and is ready to run for any set of tickers.

---

## Motivation

- Traditional quantitative finance assumes that asset prices follow a martingale process under the risk-neutral measure.  
- Empirically, deviations occur due to complex interdependencies between assets.  
- **Topological data analysis (TDA)** provides tools to quantify the “shape” of correlations using **persistent homology**.  
- By integrating **persistent homology features** with Monte Carlo pricing, we aim to detect periods where market topology indicates higher risk of pricing errors.

---

## Methodology

### 1. Data Acquisition

- Adjusted close prices are downloaded from Yahoo Finance using `yfinance`.
- Daily log returns are computed for each asset.

### 2. Correlation Networks

- Compute the correlation matrix of asset returns.  
- Convert correlations to a distance metric:  

  \[
  d_{ij} = \sqrt{2(1 - \rho_{ij})}
  \]  

  where \(\rho_{ij}\) is the Pearson correlation between assets \(i\) and \(j\)._













