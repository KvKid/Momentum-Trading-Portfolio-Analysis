# Momentum-based Portfolio Trading Strategy
This Python program implements a basic momentum-based portfolio trading strategy, fetching historical stock data from Yahoo Finance and using pandas and numpy for data manipulation.

## Installation
To run this program, you'll need Python installed along with several packages. The required packages are:

- pandas
- numpy
- yfinance
- matplotlib
- empyrical

You can install these packages using pip:
```
pip install pandas numpy yfinance matplotlib empyrical
```

## Usage
The list of stocks in the portfolio and the period for which to fetch the stock data can be modified to fit your preferences.

```
# Define the list of stocks in your portfolio
stocks = ['AAPL', 'MSFT', 'AMZN', 'GOOG', 'META']

# Define the period for which to fetch the stock data
start_date = '2020-01-01'
end_date = '2023-01-01'
```

The program calculates monthly price of the stocks and the percentage change in the prices to get the returns.

The 'calculate_momentum' function calculates the momentum value of a given series 'x' by dividing the value of 'x' at a specific time period with the value of 'x' at a shifted time period.

The 'calculate_portfolio_weights' function calculates the ranks of each stock based on their momentum. It creates a mask of stocks to be included in the portfolio by checking which stocks have ranks less than or equal to 3. It then calculates the portfolio weights by dividing the mask by the sum of the mask along the rows.

Portfolio returns are calculated based on the momentum of stocks. The program first applies the momentum function to the returns of stocks using a specific time period. Then, it calculates the portfolio weights based on the ranks of stocks' momentum. Finally, it calculates the portfolio returns by multiplying the portfolio weights with the returns and summing them along the rows.

The program also calculates and plots the rolling Sharpe Ratio, maximum drawdown over a 12 month period, and the cumulative return of the portfolio. Additionally, the cumulative return of S&P 500 is plotted as a benchmark.