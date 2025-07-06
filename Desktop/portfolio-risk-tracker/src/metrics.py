import numpy as np

def sharpe_ratio(returns, risk_free_rate=0.01):
    excess_returns = returns - risk_free_rate / 252
    return np.mean(excess_returns) / np.std(excess_returns)

def calculate_beta(stock_returns, market_returns):
    cov = np.cov(stock_returns, market_returns)[0][1]
    var_market = np.var(market_returns)
    return cov / var_market

def calculate_var(returns, confidence_level=0.95):
    return np.percentile(returns, (1 - confidence_level) * 100)
