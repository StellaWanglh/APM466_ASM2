import yfinance as yf
import numpy as np

# Function to get stock volatility
def get_stock_volatility(ticker, start_date, end_date):
    # Download historical stock data
    stock_data = yf.download(ticker, start=start_date, end=end_date)

    # Print the columns of the dataframe to debug
    print(stock_data.columns)

    # Use 'Close' if 'Adj Close' is not available
    if 'Adj Close' in stock_data.columns:
        stock_data['Daily Return'] = stock_data['Adj Close'].pct_change()
    else:
        stock_data['Daily Return'] = stock_data['Close'].pct_change()

    # Calculate daily volatility (standard deviation of daily returns)
    daily_volatility = stock_data['Daily Return'].std()

    # Annualize the volatility (assuming 252 trading days per year)
    annualized_volatility = daily_volatility * np.sqrt(252)

    return annualized_volatility

# Example usage for Magna International Inc. (MG.TO)
ticker = 'MG.TO'  # Magna International Inc. ticker symbol for Toronto Stock Exchange
start_date = '2024-01-01'
end_date = '2025-04-25'

# Get the volatility
volatility = get_stock_volatility(ticker, start_date, end_date)
print(f"The annualized volatility of {ticker} from {start_date} to {end_date} is {volatility:.4f}")
