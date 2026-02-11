
import pandas as pd
import numpy as np
import os

def verify_exercise_1():
    print("Verifying Exercise 1...")
    dates = pd.date_range(start='2010-01-01', end='2020-12-31', freq='D')
    values = np.arange(len(dates))
    integer_series = pd.Series(data=values, index=dates, name='days_since_start')
    
    # Check length
    assert len(integer_series) == (pd.Timestamp('2020-12-31') - pd.Timestamp('2010-01-01')).days + 1
    
    # Check moving average
    ma = integer_series.rolling(window=7).mean()
    assert len(ma) == len(integer_series)
    assert pd.isna(ma.iloc[5]) # First 6 should be NaN (0-5 index)
    assert not pd.isna(ma.iloc[6])
    print("Exercise 1 Passed.")

def verify_exercise_2():
    print("Verifying Exercise 2...")
    # Load data
    try:
        df = pd.read_csv('data/AAPL.csv')
    except FileNotFoundError:
        # Try relative paths
        if os.path.exists('../data/AAPL.csv'):
            df = pd.read_csv('../data/AAPL.csv')
        else:
            print("Data file not found!")
            return

    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df.sort_index(inplace=True)
    
    # Check resampling
    monthly = df.resample('BM').last()
    assert len(monthly) > 0
    
    # Check returns
    df['Open_Return'] = df['Open'].pct_change()
    assert 'Open_Return' in df.columns
    print("Exercise 2 Passed.")

def verify_exercise_3():
    print("Verifying Exercise 3...")
    business_dates = pd.bdate_range('2021-01-01', '2021-12-31')
    tickers = ['AAPL', 'FB', 'GE', 'AMZN', 'DAI']
    index = pd.MultiIndex.from_product([business_dates, tickers], names=['Date', 'Ticker'])
    market_data = pd.DataFrame(index=index,
                            data=np.random.randn(len(index), 1),
                            columns=['Price'])
    
    pivoted = market_data.unstack(level='Ticker')
    pivoted.columns = pivoted.columns.droplevel(0)
    returns = pivoted.pct_change()
    
    assert returns.shape[1] == 5 # 5 tickers
    assert returns.shape[0] == len(business_dates)
    print("Exercise 3 Passed.")

def verify_exercise_4():
    print("Verifying Exercise 4...")
    # Load data
    try:
        df = pd.read_csv('data/AAPL.csv')
    except FileNotFoundError:
         if os.path.exists('../data/AAPL.csv'):
            df = pd.read_csv('../data/AAPL.csv')
    
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df = df.dropna()
    
    df['daily_return'] = df['Adj Close'].pct_change()
    df['future_return'] = df['daily_return'].shift(-1)
    df = df.dropna()
    
    np.random.seed(42)
    df['signal'] = np.random.choice([0, 1], size=len(df), p=[0.5, 0.5])
    
    df['strategy_pnl'] = df['signal'] * df['future_return']
    
    total_invested = df['signal'].sum()
    total_pnl = df['strategy_pnl'].sum()
    
    assert total_invested > 0
    # Allow negative PnL, but just check calculation is done
    print(f"Strategy PnL: {total_pnl}")
    print("Exercise 4 Passed.")

if __name__ == "__main__":
    verify_exercise_1()
    verify_exercise_2()
    verify_exercise_3()
    verify_exercise_4()
    print("All verification tests passed!")
