
import pandas as pd
import numpy as np

def debug_randomness_v2():
    df = pd.read_csv('data/AAPL.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df.sort_index(inplace=True)
    
    print(f"Data Range: {df.index.min()} to {df.index.max()}")
    print(f"Total Rows: {len(df)}")
    
    # Audit mentions 2021-01-29 is NaN in PnL logic because it's the last day?
    # "2021-01-29 NaN"
    # This implies the dataset ends at 2021-01-29.
    
    # Calculate future return
    df['daily_return'] = df['Adj Close'].pct_change()
    df['future_return'] = (df['Adj Close'].shift(-1) - df['Adj Close']) / df['Adj Close']
    
    # Audit strategy:
    # "Drop the rows with missing values and compute the daily future return..."
    # If I compute return first, then dropna?
    
    # Let's try:
    # 1. Compute future return on full data
    # 2. Drop rows with missing values (which will drop the last row AND maybe first row if daily_return used but we use Adj Close directly)
    
    # Wait, "Drop the rows with missing values and compute..."
    # This usually means clean data first.
    # If I clean data first, I lose rows with NaNs.
    # Let's see how many NaNs are there initially.
    print(f"Initial NaNs: {df.isnull().sum().sum()}")
    
    df_dropped = df.dropna()
    print(f"After initial dropna: {len(df_dropped)}")
    
    # Now compute future return
    df_dropped['future_return'] = (df_dropped['Adj Close'].shift(-1) - df_dropped['Adj Close']) / df_dropped['Adj Close']
    
    # Now valid rows for backtest are those where future_return is not NaN
    # The last row of df_dropped will have NaN future_return
    df_valid = df_dropped.dropna(subset=['future_return'])
    
    print(f"Valid Rows for Backtest: {len(df_valid)}")
    
    np.random.seed(2712)
    # "create a Series that contains a random boolean array... using np.random.randint(0,2,len(df.index)"
    # If "df" refers to the one used for backtest?
    
    signals = np.random.randint(0, 2, len(df_valid))
    invested = signals.sum()
    pnl = (signals * df_valid['future_return']).sum()
    ret = pnl / invested
    
    print(f"Invested: {invested}")
    print(f"PnL: {pnl}")
    print(f"Return: {ret}")
    
    # Audit invested: 5147
    # My invested: ?

if __name__ == "__main__":
    debug_randomness_v2()
