import yfinance as yf
import pandas as pd
import numpy as np
from scipy.optimize import minimize

def download_data(tickers, start, end):
    data = yf.download(tickers, start=start, end=end, group_by='ticker', auto_adjust=True)
    if isinstance(tickers, str):
        df = data['Close'].to_frame(name=tickers)
    else:
        df = pd.DataFrame({ticker: data[ticker]['Close'] for ticker in tickers if ticker in data})
    return df.dropna()

def calculate_returns(price_df):
    return price_df.pct_change().dropna()

def optimize_portfolio(returns):
    num_assets = returns.shape[1]
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0, 1) for _ in range(num_assets))

    def negative_sharpe(weights):
        port_ret = np.dot(weights, returns.mean()) * 252
        port_vol = np.sqrt(np.dot(weights.T, returns.cov().dot(weights)) * 252)
        return -port_ret / port_vol

    result = minimize(negative_sharpe, num_assets * [1./num_assets], method='SLSQP', bounds=bounds, constraints=constraints)
    return result.x

def monte_carlo_simulation(prices, n_simulations=500, n_days=252):
    last_price = prices.iloc[-1].mean()
    returns = prices.pct_change().mean().mean()
    volatility = prices.pct_change().std().mean()

    simulations = np.zeros((n_simulations, n_days))

    for i in range(n_simulations):
        price = last_price
        for t in range(n_days):
            price *= np.exp((returns - 0.5 * volatility ** 2) + volatility * np.random.normal())
            simulations[i, t] = price

    return simulations

def monte_carlo_simulation_individual(prices, n_simulations=300, n_days=252):
    simulations_dict = {}
    tickers = prices.columns

    for ticker in tickers:
        last_price = prices[ticker].iloc[-1]
        mean_return = prices[ticker].pct_change().mean()
        std_dev = prices[ticker].pct_change().std()

        simulations = np.zeros((n_simulations, n_days))

        for i in range(n_simulations):
            price = last_price
            for t in range(n_days):
                price *= np.exp((mean_return - 0.5 * std_dev**2) + std_dev * np.random.normal())
                simulations[i, t] = price

        simulations_dict[ticker] = simulations

    return simulations_dict
