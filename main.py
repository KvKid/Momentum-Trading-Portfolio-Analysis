import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt
import empyrical

# Define the list of stocks in your portfolio
stocks = ['AAPL', 'MSFT', 'AMZN', 'GOOG', 'META']

# Define the period for which to fetch the stock data
start_date = '2020-01-01'
end_date = '2023-01-01'

# Fetch the stock data
data = yf.download(stocks, start=start_date, end=end_date)['Close']
sp500 = yf.download('^GSPC', start=start_date, end=end_date)


# Calculate the monthly price of the stocks
data_monthly = data.resample('M').ffill() # Use forward filling
returns = data_monthly.pct_change()

# Function to calculate momentum
def calculate_momentum(x, period):
    return (x.shift() / x.shift(period)) - 1

# Calculate portfolio allocation
def calculate_portfolio_weights(df):
    # Calculate momentum ranks
    ranks = df.rank(axis=1, ascending=False)
    
    # Create a mask of stocks to be included in the portfolio
    mask = ranks<=3

    # Calculate portfolio weights
    portfolio_weights = mask.divide(mask.sum(axis=1), axis=0)
    return portfolio_weights

# Apply the momentum function to the returns
momentum = returns.apply(calculate_momentum, args=(6,))

# Calculate portfolio weights
portfolio_weights = calculate_portfolio_weights(momentum)

# Calculate portfolio returns
portfolio_returns = (portfolio_weights * returns).sum(axis=1)

# Calculate rolling metrics
window =   12
rolling_sharpe_ratio = portfolio_returns.rolling(window).apply(empyrical.sharpe_ratio)
rolling_max_drawdown = portfolio_returns.rolling(window).apply(empyrical.max_drawdown)
portfolio_returns_cum = portfolio_returns.cumsum()

# Plot rolling Sharpe Ratio
plt.figure(figsize=(12, 6))
plt.plot(rolling_sharpe_ratio)
plt.title('Yearly Rolling Sharpe Ratio')
plt.xlabel('Date')
plt.ylabel('Sharpe Ratio')
plt.grid(True)
plt.show()

# Plot rolling Drawdown
plt.figure(figsize=(12, 6))
plt.plot(rolling_max_drawdown)
plt.title('Rolling Max Drawdown')
plt.xlabel('Date')
plt.ylabel('Max Drawdown')
plt.grid(True)
plt.show()

# Plot rolling Monthly Returns with the average return if we invested in all 5 and held.
# first find returns from s&p 500:
sp500 = yf.download('^GSPC', start=start_date, end=end_date)
sp500 = sp500['Close'].resample('M').ffill()
sp500_returns = sp500.pct_change()
fig,ax = plt.subplots(figsize = (12,6))

ax.plot(portfolio_returns_cum,label = 'Portfolio Cumulative Value')

ax.set_title('Portfolio Value over time')
ax.set_ylabel('Cumulative Return')
ax.set_xlabel('Date')
ax1 = ax.twinx()
ax.plot(sp500_returns.cumsum(),'r-',label = 'S&P 500 Bencehmark')
ax.legend()
plt.grid(True)
plt.show()



