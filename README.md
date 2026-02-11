# Time Series Analysis Project

This project simulates the role of a Quantitative Analyst at a hedge fund, focusing on manipulating and analyzing financial time series data using Python.

## Overview

The project consists of a series of exercises implemented in a Jupyter Notebook, covering:
1.  **Time Series Manipulation**: Creating and smoothing time series data.
2.  **Financial Data Analysis**: working with Apple (AAPL) stock data, including preprocessing, visualization, and return calculation.
3.  **Multi-Asset Analysis**: Handling multiple time series simultaneously.
4.  **Backtesting**: Implementing and evaluating a simple long-only trading strategy.

## Project Structure

```
time-series/
├── data/
│   └── AAPL.csv                # Financial data used for analysis
├── notebooks/
│   ├── time_series_exercises.ipynb          # Main solution notebook
│   └── time_series_exercises_executed.ipynb # Executed version of the notebook
├── scripts/
│   ├── download_data.py        # Script to download necessary data
│   ├── verify_solutions.py     # Script to verify core logic
│   └── audit_check.py          # Comprehensive audit validation script
└── README.md                   # Project documentation
```

## Setup & Installation

1.  **Prerequisites**: Ensure you have Python 3.9+ installed.
2.  **Install Dependencies**:
    ```bash
    pip install pandas numpy plotly jupyter
    ```

## Usage

### Running the Notebook
You can start Jupyter and open the main notebook:
```bash
jupyter notebook notebooks/time_series_exercises.ipynb
```

### Running Verification Scripts
To verify the solutions against the project requirements:
```bash
python3 scripts/verify_solutions.py
python3 scripts/audit_check.py
```

## Key Features Implemented
- **Vectorized Operations**: Avoided `for` loops for efficiency, using Pandas vectorized functions instead.
- **Interactive Visualization**: Used Plotly for interactive candlestick and PnL charts.
- **Robust Data Handling**: Handled missing values, resampling (Business Month End), and correct PnL calculation logic.
- **Reproducibility**: Set random seeds where appropriate (though minor environment differences may occur).

## Author
[Your Name/Username]
