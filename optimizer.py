from pypfopt import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
from pypfopt import objective_functions
import pandas as pd
import numpy as np

class PortfolioOptimizer:
    def __init__(self, prices, risk_free_rate=0.02):
        """
        Initialize the PortfolioOptimizer.
        
        Args:
            prices (pd.DataFrame): Adjusted close prices of assets.
            risk_free_rate (float): Risk-free rate for Sharpe Ratio calculation.
        """
        self.prices = prices
        self.risk_free_rate = risk_free_rate
        self.mu = None
        self.S = None
        self.weights = None
        
        self.calculate_metrics()

    def calculate_metrics(self):
        """Calculates expected returns and sample covariance."""
        # Calculate expected returns (mean historical returns)
        self.mu = expected_returns.mean_historical_return(self.prices)
        
        # Calculate covariance matrix
        self.S = risk_models.sample_cov(self.prices)

    def optimize_max_sharpe(self):
        """
        Optimizes for the maximum Sharpe Ratio.
        
        Returns:
            dict: Optimal weights.
        """
        ef = EfficientFrontier(self.mu, self.S)
        
        # Objective: Maximize Sharpe Ratio
        weights = ef.max_sharpe(risk_free_rate=self.risk_free_rate)
        cleaned_weights = ef.clean_weights()
        self.weights = cleaned_weights
        
        simulation_results = ef.portfolio_performance(verbose=True, risk_free_rate=self.risk_free_rate)
        
        return cleaned_weights, simulation_results

    def optimize_min_volatility(self):
        """
        Optimizes for minimum volatility.
        
        Returns:
            dict: Optimal weights.
        """
        ef = EfficientFrontier(self.mu, self.S)
        
        weights = ef.min_volatility()
        cleaned_weights = ef.clean_weights()
        self.weights = cleaned_weights
        
        simulation_results = ef.portfolio_performance(verbose=True, risk_free_rate=self.risk_free_rate)
        
        return cleaned_weights, simulation_results
        
    def get_current_metrics(self):
        """Returns the calculated mean returns and covariance."""
        return self.mu, self.S
