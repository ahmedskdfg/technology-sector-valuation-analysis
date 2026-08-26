import pandas as pd
import yfinance as yf


TICKERS = ["AAPL", "MSFT", "GOOGL", "NVDA", "AMZN"]


def latest_value(statement: pd.DataFrame, names: list[str]) -> float | None:
    """Return the newest available value for the first matching statement row."""
    for name in names:
        if name in statement.index:
            values = statement.loc[name].dropna()
            if not values.empty:
                return float(values.iloc[0])
    return None


def get_company_data(symbol: str) -> dict[str, object]:
    ticker = yf.Ticker(symbol)
    info = ticker.info
    balance_sheet = ticker.balance_sheet
    income_statement = ticker.income_stmt

    return {
        "Ticker": symbol,
        "Market Cap": info.get("marketCap"),
        "Total Debt": latest_value(balance_sheet, ["Total Debt"]),
        "Cash": latest_value(
            balance_sheet,
            [
                "Cash Cash Equivalents And Short Term Investments",
                "Cash And Cash Equivalents",
            ],
        ),
        "Revenue": latest_value(income_statement, ["Total Revenue"]),
        "EBITDA": latest_value(income_statement, ["EBITDA"]),
        "P / E": info.get("trailingPE"),
    }


rows = []
for symbol in TICKERS:
    try:
        rows.append(get_company_data(symbol))
    except Exception as error:
        print(f"Could not retrieve {symbol}: {error}")

comparison = pd.DataFrame(rows).set_index("Ticker")
financial_columns = ["Market Cap", "Total Debt", "Cash", "Revenue", "EBITDA"]
comparison[financial_columns] = comparison[financial_columns].apply(
    pd.to_numeric, errors="coerce"
)
comparison["P / E"] = pd.to_numeric(comparison["P / E"], errors="coerce")
comparison["Enterprise Value"] = (
    comparison["Market Cap"] + comparison["Total Debt"] - comparison["Cash"]
)
comparison["EV / EBITDA"] = comparison["Enterprise Value"] / comparison["EBITDA"]
comparison["EV / Sales"] = comparison["Enterprise Value"] / comparison["Revenue"]

valuation_columns = ["Enterprise Value", "EV / EBITDA", "EV / Sales", "P / E"]

print("Technology sector comparison (latest available annual data)\n")
print(
    comparison[financial_columns + valuation_columns].to_string(
        float_format=lambda value: f"{value:,.2f}"
    )
)

multiple_columns = ["EV / EBITDA", "EV / Sales", "P / E"]
sector_multiples = comparison[multiple_columns]
sector_summary = sector_multiples.agg(["mean", "median"]).T

print("\nSector multiple summary")
print(sector_summary.to_string(float_format=lambda value: f"{value:,.2f}x"))
