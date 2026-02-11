
import pandas as pd
import numpy as np

def debug_randomness():
    df = pd.read_csv('data/AAPL.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df.sort_index(inplace=True)
    
    # Calculate future return
    df['daily_return'] = df['Adj Close'].pct_change()
    df['future_return'] = df['daily_return'].shift(-1)
    
    # Drop where future_return is NaN (last row) -> This is important!
    # The audit says: "Drop the rows with missing values AND compute..."
    # If we drop missing values first, then compute logic might change?
    # Audit: "Drop the rows with missing values and compute the daily future return..."
    # Does it mean drop missing in original data first?
    # Let's try matching exact steps.
    
    missing_before = df.isnull().sum().sum()
    df.dropna(inplace=True)
    
    # Recompute returns on clean data?
    # "Drop the rows with missing values and compute the daily future return... on the adjusted close price."
    # If I drop NA, I might break the time series continuity? But audit says "Drop... and compute".
    # Let's try:
    # 1. Drop NA
    # 2. Compute future return
    
    df['daily_return'] = df['Adj Close'].pct_change()
    df['future_return'] = df['daily_return'].shift(-1)
    
    # Remove the last row which is now NaN due to shift
    df_clean = df.dropna(subset=['future_return']).copy()
    
    print(f"Length of clean df: {len(df_clean)}")
    
    # Try different random methods with seed 2712
    seeds = [2712]
    for seed in seeds:
        print(f"--- Seed {seed} ---")
        np.random.seed(seed)
        
        # Method 1: randint
        s1 = np.random.randint(0, 2, len(df_clean))
        invested1 = s1.sum()
        pnl1 = (s1 * df_clean['future_return']).sum()
        ret1 = pnl1 / invested1
        print(f"Randint Return: {ret1}")
        
        # Method 2: choice
        np.random.seed(seed)
        s2 = np.random.choice([0, 1], size=len(df_clean), p=[0.5, 0.5])
        invested2 = s2.sum()
        pnl2 = (s2 * df_clean['future_return']).sum()
        ret2 = pnl2 / invested2
        print(f"Choice Return: {ret2}")
        
        # Method 3: maybe len(df) instead of len(df_clean)?
        # Audit says: "is the index of the Series the same as the index of the DataFrame? The data of the series can be generated using np.random.randint(0,2,len(df.index)."
        # If I generate for full df then subset?
        np.random.seed(seed)
        full_signals = np.random.randint(0, 2, len(df))
        df['signal'] = full_signals
        # Recalculate based on df_clean logic (taking signal where future_return exists)
        df_merged = df.dropna(subset=['future_return'])
        
        invested3 = df_merged['signal'].sum()
        pnl3 = (df_merged['signal'] * df_merged['future_return']).sum()
        ret3 = pnl3 / invested3
        print(f"Full Len Randint Return: {ret3}")

if __name__ == "__main__":
    debug_randomness()
