
# 📈 Portfolio Risk Tracker

An interactive web-based dashboard built with **Python** and **Streamlit** to evaluate portfolio performance, analyze financial risk metrics, and simulate future stock prices using **Monte Carlo methods** and **Sharpe-ratio maximizing optimization**.

---

## 🔍 Features

### 📊 Portfolio Analysis
- Download historical stock data using `yFinance`
- Visualize daily closing prices and returns
- Calculate:
  - ✅ Annualized Return
  - ✅ Annualized Volatility
  - ✅ Sharpe Ratio
  - ✅ Beta
  - ✅ Value at Risk (VaR 95%)

### 🔄 Portfolio Optimization
- Uses `scipy.optimize` to calculate asset weights
- Maximizes Sharpe Ratio subject to constraints
- Displays optimal allocation based on selected tickers

### 🔮 Monte Carlo Simulations
- 📈 Simulate **future price paths of the entire portfolio**
- 📉 Run **individual stock price simulations**
- Adjustable:
  - Number of simulations (e.g. 300–1000)
  - Number of prediction days (e.g. 30–365)

### 💡 User Features
- Built using Streamlit for real-time interactivity
- Easy-to-use input panel: just enter stock tickers and dates
- Graphs powered by `matplotlib` + `Streamlit`

---

## 🛠️ Tech Stack

| Tool / Library   | Purpose                            |
|------------------|-------------------------------------|
| Python           | Core programming language           |
| Streamlit        | Web interface & dashboard           |
| yfinance         | Historical stock data               |
| NumPy / Pandas   | Data manipulation & math            |
| Matplotlib       | Charting & visualization            |
| SciPy            | Optimization (Sharpe Maximization)  |

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/portfolio-risk-tracker.git
cd portfolio-risk-tracker
