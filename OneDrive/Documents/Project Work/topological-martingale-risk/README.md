\# Topological Martingale Risk



\*\*Author:\*\* Zacharia Moussallati  

\*\*Date:\*\* 2025-08-31



---



\## Overview



This project investigates the relationship between \*\*market correlation topology\*\* and \*\*martingale-based pricing errors\*\* using historical stock data. By combining \*\*topological data analysis (TDA)\*\* with \*\*Monte Carlo martingale simulations\*\*, we explore whether structural changes in asset correlations can predict deviations in pricing models.  



The pipeline is fully automated, from data acquisition to integration and plotting, and is ready to run for any set of tickers.



---



\## Motivation



\- Traditional quantitative finance assumes that asset prices follow a martingale process under the risk-neutral measure.  

\- Empirically, deviations occur due to complex interdependencies between assets.  

\- \*\*Topological data analysis (TDA)\*\* provides tools to quantify the “shape” of correlations using \*\*persistent homology\*\*.  

\- By integrating \*\*persistent homology features\*\* with Monte Carlo pricing, we aim to detect periods where market topology indicates higher risk of pricing errors.



---



\## Methodology



\### 1. Data Acquisition



\- Adjusted close prices are downloaded from Yahoo Finance using `yfinance`.

\- Daily log returns are computed for each asset.



\### 2. Correlation Networks



\- Compute the correlation matrix of asset returns.  

\- Convert correlations to a distance metric:  

&nbsp; \\\[

&nbsp; d\_{ij} = \\sqrt{2(1 - \\rho\_{ij})}

&nbsp; \\]  

&nbsp; where \\(\\rho\_{ij}\\) is the Pearson correlation between assets \\(i\\) and \\(j\\).  

\- Construct a \*\*Minimum Spanning Tree (MST)\*\* to visualise the correlation network.



\### 3. Topological Analysis (TDA)



\- Use \*\*Vietoris-Rips persistence\*\* to compute \*\*0D and 1D homology\*\* of the correlation distance matrix.  

\- Key features:

&nbsp; - \*\*H0\*\*: connected components (Betti0)  

&nbsp; - \*\*H1\*\*: loops (Betti1 / persistence intervals)

\- Instead of counting features, we compute \*\*H1 total persistence\*\*:

&nbsp; \\\[

&nbsp; \\text{H1 Total Persistence} = \\sum\_{i} (\\text{death}\_i - \\text{birth}\_i)

&nbsp; \\]  

&nbsp; This measures the “strength” of loop structures in the correlation network.



\### 4. Monte Carlo Martingale Pricing



\- For each rolling window of returns:

&nbsp; - Simulate asset paths under a simple martingale assumption:

&nbsp;   \\\[

&nbsp;   S\_{t+\\Delta t} = S\_t \\exp\\Big((\\mu - 0.5\\sigma^2)\\Delta t + \\sigma \\sqrt{\\Delta t} Z\_t\\Big), \\quad Z\_t \\sim N(0,1)

&nbsp;   \\]  

&nbsp;   where \\(S\_t\\) is the price, \\(\\mu = 0\\), and \\(\\sigma\\) is estimated from returns.  

&nbsp; - Compute the \*\*mean Monte Carlo terminal price\*\* and compare it to observed returns.  

&nbsp; - Define \*\*pricing error\*\* as the absolute difference:

&nbsp;   \\\[

&nbsp;   \\text{Pricing Error} = | \\text{MC Price} - \\text{Observed Mean Price} |

&nbsp;   \\]



\### 5. Integration



\- For each rolling window:

&nbsp; - Compute \*\*H1 total persistence\*\* from topology analysis.  

&nbsp; - Compute \*\*Monte Carlo pricing error\*\* for the same window.  

\- Produce a \*\*scatter plot\*\* of `H1 Total Persistence` vs `Pricing Error`.  

\- Save integration results as CSV for further analysis.



---



\## Installation



```bash

\# Clone repository

git clone https://github.com/yourusername/topological-martingale-risk.git

cd topological-martingale-risk



\# Create virtual environment (recommended)

python -m venv .venv

source .venv/Scripts/activate   # Windows

source .venv/bin/activate       # Linux/Mac



\# Install dependencies

pip install -r requirements.txt



\## Usage:

python main.py --tickers AAPL MSFT AMZN GOOGL META --start 2015-01-01 --end 2025-08-01



Outputs:



results/summaries/: CSVs of prices, returns, persistence diagrams, Monte Carlo pricing, and integration results



results/plots/: MST plots, persistence histograms, and Betti vs Price scatter plots



Example plots:



mst.png: Correlation network



persistence.png: Histogram of H0/H1 lifetimes



h1\_total\_vs\_price.png: H1 Total Persistence vs Pricing Error





\## Directory Structure



topological-martingale-risk/

├─ main.py                  # Orchestrates pipeline

├─ requirements.txt

├─ README.md

├─ notebooks/

│  ├─ 01\_data\_prep.py

│  ├─ 02\_correlation\_networks.py

│  ├─ 03\_topology\_analysis.py

│  ├─ 04\_martingale\_pricing.py

│  └─ 05\_integration\_results.py

└─ results/

&nbsp;  ├─ summaries/

&nbsp;  └─ plots/





\## Derivation Notes



1\. \*\*Correlation distance\*\*: transforms correlation to Euclidean-like distance suitable for TDA.  

2\. \*\*Persistent homology\*\*: captures multi-scale topological features of the correlation network.  

3\. \*\*Monte Carlo pricing\*\*: simple discrete-time GBM under martingale assumption.  

4\. \*\*Rolling window\*\*: ensures temporal variation and produces meaningful scatter plots rather than a single point.  

5\. \*\*Integration metric\*\*: `H1 Total Persistence` correlates structural loops in the correlation network with deviations in martingale pricing.



---



\## Results / Interpretation



\- Scatter plots reveal periods where \*\*high H1 total persistence\*\* coincides with \*\*larger pricing errors\*\*.  

\- This suggests that \*\*complex correlation structures (loops) may signal higher risk\*\* in martingale pricing.  

\- MST and persistence histograms provide visual verification of the evolving market topology.



---



\## Future Improvements



1\. Include \*\*H0 and H1 combined features\*\* (e.g., ratios, max persistence).  

2\. Use \*\*multi-asset Monte Carlo simulation\*\* with realistic covariance.  

3\. Apply \*\*alternative TDA methods\*\* like \*\*persistent landscapes\*\* or \*\*persistence images\*\*.  

4\. Backtest against actual derivative prices to quantify predictive power.



---



\## References



\- Carlsson, G. (2009). \_Topology and data\_. Bulletin of the American Mathematical Society, 46(2), 255–308.  

\- Chazal, F., et al. (2017). \_GUDHI: Geometry Understanding in Higher Dimensions\_. Journal of Machine Learning Research.  

\- Adams, H., et al. (2017). \_Persistence images: A stable vector representation of persistent homology\_. Journal of Machine Learning Research.  

\- Yahoo Finance API: \[https://pypi.org/project/yfinance/](https://pypi.org/project/yfinance/)



---



\## License



MIT License













