# Author: j4c0b1
# GitHub: https://github.com/cj4c0b1
# Donations (EVM): 0x7B267EcEc11a07CA2a782E4b8a51558a70449e7c

import yfinance as yf
import pandas as pd
import numpy as np

def fetch_data(tickers, start_date='2018-01-01', end_date='2023-01-01'):
    """
    Fetches adjusted close prices for the given tickers.
    
    Args:
        tickers (list): List of ticker symbols (e.g., ['AAPL', 'MSFT']).
        start_date (str): Start date for data.
        end_date (str): End date for data.
        
    Returns:
        pd.DataFrame: DataFrame containing adjusted close prices.
    """
    print(f"Fetching data for {tickers} from {start_date} to {end_date}...")
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    
    # Check if data is empty
    if data.empty:
        raise ValueError("No data fetched. Please check tickers or date range.")
    
    # Handle missing values (simple forward fill then backward fill)
    data = data.ffill().bfill()
    
    return data

def generate_synthetic_data(n_assets=5, n_days=1000, seed=42):
    """
    Generates synthetic price data for testing.
    
    Args:
        n_assets (int): Number of assets.
        n_days (int): Number of days.
        seed (int): Random seed.
        
    Returns:
        pd.DataFrame: DataFrame of synthetic prices.
    """
    np.random.seed(seed)
    returns = np.random.normal(0.0005, 0.01, (n_days, n_assets))
    prices = 100 * np.cumprod(1 + returns, axis=0)
    
    tickers = [f"ASSET_{i}" for i in range(1, n_assets + 1)]
    dates = pd.date_range(start='2020-01-01', periods=n_days, freq='D')
    
    df = pd.DataFrame(prices, index=dates, columns=tickers)
    return df

if __name__ == "__main__":
    # Test
    tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'TSLA']
    try:
        df = fetch_data(tickers)
        print("Fetched Data Shape:", df.shape)
        print(df.head())
    except Exception as e:
        print(f"Error fetching data: {e}")
        print("Generating synthetic data instead...")
        df = generate_synthetic_data()
        print(df.head())
