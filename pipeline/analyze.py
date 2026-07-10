import pandas as pd
import numpy as np

def analyze_price_trend(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the long-term price trend and key growth milestones for Apple stock.
    
    Parameters:
        df (pd.DataFrame): Cleaned Apple stock historical data.
        
    Returns:
        pd.DataFrame: A DataFrame containing Date and Close price for trend mapping.
    """
    return df[['Date', 'Close']]


def analyze_daily_returns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates daily percentage returns to measure market risk and volatility.
    
    Parameters:
        df (pd.DataFrame): Cleaned Apple stock historical data.
        
    Returns:
        pd.DataFrame: A DataFrame with Date and Daily_Return percentages (excluding NaNs).
    """
    df_copy = df.copy()
    df_copy['Daily_Return'] = df_copy['Close'].pct_change() * 100
    return df_copy[['Date', 'Daily_Return']].dropna()


def analyze_monthly_volume(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregates trading volume by Year-Month to identify seasonal investor trading behavior.
    
    Parameters:
        df (pd.DataFrame): Cleaned Apple stock historical data.
        
    Returns:
        pd.DataFrame: Aggregated DataFrame grouped by YearMonth with average trading volume.
    """
    # Grouping by year-month to uncover seasonal trends like iPhone launch months
    monthly_data = df.groupby('YearMonth')['Volume'].mean().reset_index()
    return monthly_data


def analyze_volume_by_direction(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compares the average trading volume on positive (Up) days versus negative (Down) days
    to evaluate investor psychology (FOMO vs Panic Selling).
    
    Parameters:
        df (pd.DataFrame): Cleaned Apple stock historical data.
        
    Returns:
        pd.DataFrame: Aggregated DataFrame comparing average volume across market directions.
    """
    df_copy = df.copy()
    
    # Classify the trading day based on price movement direction
    df_copy['Direction'] = np.where(df_copy['Close'] > df_copy['Open'], 'Up Day (Green)', 'Down Day (Red)')
    
    direction_data = df_copy.groupby('Direction')['Volume'].mean().reset_index()
    return direction_data