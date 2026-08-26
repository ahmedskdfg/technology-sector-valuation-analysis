# Technology Sector Valuation Analysis

A Python comparable-company analysis of five large technology companies using live financial data from Yahoo Finance through `yfinance`.

## Companies

- Apple (`AAPL`)
- Microsoft (`MSFT`)
- Alphabet (`GOOGL`)
- NVIDIA (`NVDA`)
- Amazon (`AMZN`)

## Metrics

The script extracts market capitalization, total debt, cash, revenue, EBITDA, and trailing P/E. It then calculates:

$$
\text{Enterprise Value} = \text{Market Cap} + \text{Total Debt} - \text{Cash}
$$

$$
\text{EV / EBITDA} = \frac{\text{Enterprise Value}}{\text{EBITDA}}, \qquad
\text{EV / Sales} = \frac{\text{Enterprise Value}}{\text{Revenue}}
$$

It also calculates the sector mean and median for EV / EBITDA, EV / Sales, and P / E. Comparing the mean with the median helps identify the effect of unusually high or low company valuations.

## Sample output

The following output was produced by running the script on 26 August 2026. Values are based on the latest available data returned by Yahoo Finance at that time.

```text
Sector multiple summary
              mean  median
EV / EBITDA 24.94x  23.11x
EV / Sales  11.98x  10.94x
P / E       26.67x  27.39x
```

The company-level table printed by the script includes all five financial metrics, enterprise value, and each valuation multiple.

## Run locally

```bash
pip install pandas yfinance
python tech_sector_valuation.py
```

## Notes

- Yahoo Finance data is retrieved at runtime and may change.
- Financial statement values are the newest available annual values returned by `yfinance`.
- Missing values are converted to `NaN` so one unavailable metric does not break the full comparison.
- This is an educational research project, not investment advice.

## CV description

**Technology Sector Valuation Analysis | Python, Pandas, yfinance**

Built a comparable-company valuation analysis of Apple, Microsoft, Alphabet, NVIDIA, and Amazon; extracted market cap, debt, cash, revenue, EBITDA, and P/E data; calculated enterprise value and trading multiples; and used sector mean and median multiples to assess relative valuation and identify outliers.
