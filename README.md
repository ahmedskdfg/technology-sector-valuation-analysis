# Technology Sector Valuation Analysis

A Python project combining comparable-company valuation analysis with a Monte Carlo stock-price simulation using Yahoo Finance data.

## Companies

- Apple (`AAPL`)
- Microsoft (`MSFT`)
- Alphabet (`GOOGL`)
- NVIDIA (`NVDA`)
- Amazon (`AMZN`)

## Comparable-company analysis

The valuation script extracts market capitalization, total debt, cash, revenue, EBITDA, and trailing P/E. It then calculates:

$$
\text{Enterprise Value} = \text{Market Cap} + \text{Total Debt} - \text{Cash}
$$

$$
\text{EV / EBITDA} = \frac{\text{Enterprise Value}}{\text{EBITDA}}, \qquad
\text{EV / Sales} = \frac{\text{Enterprise Value}}{\text{Revenue}}
$$

It also calculates the sector mean and median for EV / EBITDA, EV / Sales, and P / E. Comparing the mean with the median helps show how unusually high or low company valuations affect the average.

## Monte Carlo simulation

The Monte Carlo script uses Apple historical prices to estimate daily log returns, annual drift, and annual volatility. It then simulates 1,000 possible one-year price paths using a geometric Brownian motion model.

For each trading day, the simulation updates the price using:

$$
S_{t+\Delta t}=S_t\exp\left[\left(\mu-\frac{1}{2}\sigma^2\right)\Delta t+\sigma\sqrt{\Delta t}Z\right]
$$

where:

- $S_t$ is the current simulated stock price
- $\mu$ is estimated annual drift
- $\sigma$ is estimated annual volatility
- $\Delta t = 1/252$ represents one trading day
- $Z$ is a random draw from a standard normal distribution

The script then reports the mean, median, 5th percentile, and 95th percentile of the simulated one-year ending prices.

It also generates two plots:

- `monte_carlo_paths.png` showing 50 sample simulated price paths
- `ending_price_distribution.png` showing the distribution of all simulated ending prices

These image files are created when the Monte Carlo script is run locally.

## Sample valuation output

The following output was produced by running the valuation script on 26 August 2026. Values are based on the latest available data returned by Yahoo Finance at that time.

```text
Sector multiple summary
              mean  median
EV / EBITDA 24.94x  23.11x
EV / Sales  11.98x  10.94x
P / E       26.67x  27.39x
```

## Run locally

```bash
pip install pandas numpy matplotlib yfinance
python tech_sector_valuation.py
python monte_carlo_simulation.py
```

## Notes

- Yahoo Finance data is retrieved at runtime and may change.
- Financial statement values are the newest available annual values returned by `yfinance`.
- Missing values are converted to `NaN` so one unavailable metric does not break the full comparison.
- Monte Carlo output depends on model assumptions and historical estimates and is not a guarantee of future prices.
- The project is educational and not investment advice.

## CV description

**Technology Sector Valuation Analysis | Python, Pandas, NumPy, yfinance, Matplotlib**

Built a comparable-company valuation analysis of Apple, Microsoft, Alphabet, NVIDIA, and Amazon; extracted market cap, debt, cash, revenue, EBITDA, and P/E data; calculated enterprise value and trading multiples; and extended the project with a geometric Brownian motion Monte Carlo simulation using historical log returns, estimated drift and volatility, and visualisations of simulated price paths and ending-price distributions.
