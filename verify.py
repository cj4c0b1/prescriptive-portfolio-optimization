import pandas as pd
from data_generator import generate_synthetic_data
from optimizer import PortfolioOptimizer
from analysis import calculate_portfolio_performance, stress_test

def run_verification():
    print("1. Generating Data...")
    df_prices = generate_synthetic_data(n_assets=5, n_days=500, seed=42)
    df_returns = df_prices.pct_change().dropna()
    print("   Data generated successfully.")

    print("2. Optimizing Portfolio...")
    optimizer = PortfolioOptimizer(df_prices)
    weights, results = optimizer.optimize_max_sharpe()
    print("   Optimization successful.")
    print("   Weights:", weights)
    print(f"   Expected Return: {results[0]:.4f}, Volatility: {results[1]:.4f}, Sharpe: {results[2]:.4f}")

    print("3. Analyzing Performance...")
    # Baseline (Equal Weights)
    n_assets = len(df_prices.columns)
    baseline_weights = {col: 1/n_assets for col in df_prices.columns}
    base_metrics = calculate_portfolio_performance(baseline_weights, df_returns)
    print("   Baseline Sharpe:", base_metrics['Sharpe Ratio'])

    assert results[2] >= base_metrics['Sharpe Ratio'], "Optimization failed to improve Sharpe Ratio!"
    print("   SUCCESS: Optimized Sharpe > Baseline Sharpe")

    print("4. Running Stress Test...")
    scenarios = {'Crash': -0.20}
    stress_results = stress_test(weights, df_returns, scenarios)
    print(stress_results)
    print("   Stress test completed.")

if __name__ == "__main__":
    run_verification()
