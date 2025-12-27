# Prescriptive Portfolio Optimization

A Python-based prescriptive analytics solution for portfolio optimization. This project uses **Mean-Variance Optimization (MVO)** and the **PyPortfolioOpt** library to generate actionable asset allocation recommendations that maximize risk-adjusted returns (Sharpe Ratio).

## 🚀 Features

- **Synthetic Data Generation**: Create realistic financial datasets for testing and development.
- **Robust Optimization**: Uses `PyPortfolioOpt` to calculate the Efficient Frontier and maximize the Sharpe Ratio.
- **Performance Analysis**: Compare optimized portfolios against equal-weighted baselines.
- **Stress Testing**: Simulate portfolio performance under market crashes or other custom scenarios.
- **Reproducible Workflow**: Includes a Jupyter Notebook (`main.ipynb`) that serves as a technical memo and execution engine.

## 🛠️ Installation

1.  **Clone the repository**:

    ```bash
    git clone https://github.com/cj4c0b1/prescriptive-portfolio-optimization.git
    cd prescriptive-portfolio-optimization
    ```

2.  **Create a virtual environment** (recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## 📖 Usage

### Running the Technical Notebook

The core analysis is contained in `main.ipynb`. You can run it locally to see the end-to-end process:

```bash
jupyter notebook main.ipynb
```

### Running the Verification Script

To quickly verify that the optimization logic is working correctly without opening Jupyter:

```bash
python verify.py
```

## 📂 Project Structure

- `data_generator.py`: Module to fetch real market data (via `yfinance`) or generate synthetic data.
- `optimizer.py`: Wraps the optimization logic.
- `analysis.py`: Helper functions for calculating metrics, cumulative returns, and stress tests.
- `main.ipynb`: The main interactive report.

## 📊 Example Results

On a synthetic dataset of 5 assets, the model typically achieves:

- **Baseline Sharpe Ratio**: ~2.69
- **Optimized Sharpe Ratio**: ~3.24

_(Note: Results will vary based on the random seed or real-world data used.)_

## 📝 License

This project is open-source and available under the MIT License.
