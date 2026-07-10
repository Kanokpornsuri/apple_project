import pandas as pd

def clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the Apple stock DataFrame, fix naming, and force text prices into actual numbers.
    Takes: Raw DataFrame
    Returns: Cleaned DataFrame with correct numeric data types
    """
    # Create a safe copy of the data to avoid unexpected warnings
    df = df.copy()
    
    # 1. Clean the empty spaces out of column headers
    df.columns = df.columns.str.strip()
    # 2. Rename the closing price column to standard 'Close'
    df = df.rename(columns={'Close/Last': 'Close'})
    
    # 3. Clean and force price/volume columns to become actual numbers
    numeric_columns = ['Close', 'Open', 'High', 'Low', 'Volume']
    for col in numeric_columns:
        if col in df.columns:
            # First, convert column to clean text strings
            df[col] = df[col].astype(str).str.strip()
            # Remove dollar signs ($) so '$135.25' becomes '135.25'
            df[col] = df[col].str.replace('$', '', regex=False)
            # Force convert the clean text into actual mathematical numbers
            df[col] = pd.to_numeric(df[col], errors='coerce')
            
    # 4. Drop any rows with empty values or rows that failed number conversion
    df = df.dropna()
    
    # 5. Convert 'Date' to datetime objects for timeline calculations
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])
    # 6. Sort rows from oldest to newest date so math flows forward in time
    df = df.sort_values('Date')
    
    # 7. Create a 'YearMonth' category column for monthly group analysis
    df['YearMonth'] = df['Date'].dt.to_period('M').astype(str)
    
    return df