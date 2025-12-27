# Author: j4c0b1
# GitHub: https://github.com/cj4c0b1
# Donations (EVM): 0x7B267EcEc11a07CA2a782E4b8a51558a70449e7c

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_portfolio_performance(weights, returns, risk_free_rate=0.02):
    """
    Calculates the annualized return, volatility, and Sharpe ratio of a portfolio.
    
    Args:
        weights (dict): Asset weights.
        returns (pd.DataFrame): Historical daily returns.
        risk_free_rate (float): Risk-free rate.
        
    Returns:
        pd.Series: Performance metrics.
    """
    # Convert weights to array aligned with returns columns
    weight_arr = np.array([weights.get(col, 0) for col in returns.columns])
    
    # Calculate portfolio daily returns
    portfolio_daily_returns = returns.dot(weight_arr)
    
    # Annualized metrics (assuming 252 trading days)
    ann_return = portfolio_daily_returns.mean() * 252
    ann_volatility = portfolio_daily_returns.std() * np.sqrt(252)
    sharpe_ratio = (ann_return - risk_free_rate) / ann_volatility
    
    return pd.Series({
        "Annualized Return": ann_return,
        "Annualized Volatility": ann_volatility,
        "Sharpe Ratio": sharpe_ratio
    })

def stress_test(weights, returns, scenarios, risk_free_rate=0.02):
    """
    Simulates portfolio performance under different stress scenarios.
    
    Args:
        weights (dict): Portfolio weights.
        returns (pd.DataFrame): Historical returns.
        scenarios (dict): Dictionary of scenarios {name: return_adjustment_factor}. 
                          e.g., {'Market Crash': -0.20} -> drops all returns by 20% (simplistic)
                          OR better: specific periods like '2008-Crash'.
                          
    Returns:
        pd.DataFrame: Performance under each scenario.
    """
    results = {}
    weight_arr = np.array([weights.get(col, 0) for col in returns.columns])
    
    # Base Case
    base_perf = calculate_portfolio_performance(weights, returns, risk_free_rate)
    results['Base Case'] = base_perf
    
    for name, factor in scenarios.items():
        # A simple stress test: assumes correlation structure holds, but returns are shocked
        # This is a linear shock to expected returns for the period
        
        # Method 2: Filter specific high-volatility periods if data allows
        # But here we apply a simple shock to the annualized return
        
        shocked_return = base_perf['Annualized Return'] * (1 + factor)
        # Volatility usually increases in stress, let's assume 1.5x volatility for negative scenarios
        shocked_vol = base_perf['Annualized Volatility'] * (1.5 if factor < 0 else 1.0)
        
        shocked_sharpe = (shocked_return - risk_free_rate) / shocked_vol
        
        results[name] = pd.Series({
            "Annualized Return": shocked_return,
            "Annualized Volatility": shocked_vol,
            "Sharpe Ratio": shocked_sharpe
        })
        
    return pd.DataFrame(results)

def plot_performance_comparison(baseline_perf, optimized_perf):
    """
    Plots a bar chart comparing baseline and optimized portfolios.
    """
    df = pd.DataFrame({'Baseline': baseline_perf, 'Optimized': optimized_perf})
    
    ax = df.plot(kind='bar', figsize=(10, 6), rot=0, title='Portfolio Comparison')
    ax.set_ylabel('Value')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

def get_cumulative_returns(weights, returns):
    """
    Calculates cumulative returns for the portfolio.
    """
    weight_arr = np.array([weights.get(col, 0) for col in returns.columns])
    portfolio_daily_returns = returns.dot(weight_arr)
    cumulative_returns = (1 + portfolio_daily_returns).cumprod()
    return cumulative_returns
