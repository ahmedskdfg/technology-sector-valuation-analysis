import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

SYMBOL = "AAPL"
TRADING_DAYS = 252
SIMULATIONS = 1000
HISTORY_PERIOD = "2y"


def get_price_history(symbol: str):
    data = yf.download(symbol, period=HISTORY_PERIOD, auto_adjust=True, progress=False)
    close_prices = data["Close"]
    if hasattr(close_prices, "columns"):
        close_prices = close_prices.iloc[:, 0]
    return close_prices.dropna()


def estimate_gbm_parameters(close_prices):
    log_returns = np.log(close_prices / close_prices.shift(1)).dropna()
    mu = log_returns.mean() * TRADING_DAYS
    sigma = log_returns.std() * np.sqrt(TRADING_DAYS)
    return mu, sigma


def simulate_paths(start_price: float, mu: float, sigma: float):
    dt = 1 / TRADING_DAYS
    paths = np.zeros((TRADING_DAYS + 1, SIMULATIONS))
    paths[0] = start_price

    for day in range(1, TRADING_DAYS + 1):
        z = np.random.normal(0, 1, SIMULATIONS)
        drift = (mu - 0.5 * sigma**2) * dt
        random_shock = sigma * np.sqrt(dt) * z
        paths[day] = paths[day - 1] * np.exp(drift + random_shock)

    return paths


close_prices = get_price_history(SYMBOL)
start_price = float(close_prices.iloc[-1])
mu, sigma = estimate_gbm_parameters(close_prices)
paths = simulate_paths(start_price, mu, sigma)
ending_prices = paths[-1]

print(f"Symbol: {SYMBOL}")
print(f"Starting price: {start_price:.2f}")
print(f"Estimated annual drift: {mu:.2%}")
print(f"Estimated annual volatility: {sigma:.2%}")
print(f"Mean simulated ending price: {ending_prices.mean():.2f}")
print(f"Median simulated ending price: {np.median(ending_prices):.2f}")
print(f"5th percentile: {np.percentile(ending_prices, 5):.2f}")
print(f"95th percentile: {np.percentile(ending_prices, 95):.2f}")

plt.figure(figsize=(10, 6))
plt.plot(paths[:, :50])
plt.title(f"{SYMBOL} Monte Carlo price paths")
plt.xlabel("Trading day")
plt.ylabel("Price")
plt.tight_layout()
plt.savefig("monte_carlo_paths.png", dpi=150)
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(ending_prices, bins=40)
plt.axvline(ending_prices.mean(), linestyle="--", label="Mean")
plt.axvline(np.median(ending_prices), linestyle="--", label="Median")
plt.title(f"{SYMBOL} simulated one-year ending prices")
plt.xlabel("Ending price")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.savefig("ending_price_distribution.png", dpi=150)
plt.show()
