import pandas as pd
import matplotlib.pyplot as plt

def plot_price_trend(df: pd.DataFrame) -> plt.Figure:
    """
    Generates a premium line plot of Apple's historical stock price growth.
    """
    fig, ax = plt.subplots(figsize=(11, 5))
    
    ax.plot(df['Date'], df['Close'], color='#2c3e50', linewidth=2, label='AAPL Price')
    
    # Highlight historical macro events or peaks inside your dataset
    ax.set_title("Apple Inc. (AAPL) Historical Price Evolution", fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Timeline", fontsize=11)
    ax.set_ylabel("Stock Price (USD)", fontsize=11)
    ax.grid(True, linestyle=':', alpha=0.6, color='#95a5a6')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    return fig


def plot_daily_returns_distribution(df: pd.DataFrame) -> plt.Figure:
    """
    Generates a high-quality distribution histogram showing risk profiles and market shocks.
    """
    fig, ax = plt.subplots(figsize=(11, 5))
    
    # Plotting risk distribution with modern slate color
    n, bins, patches = ax.hist(df['Daily_Return'], bins=60, color='#7f8c8d', edgecolor='#ffffff', alpha=0.85)
    
    # Add a vertical line at 0% to explicitly separate wins from losses
    ax.axvline(x=0, color='#d35400', linestyle='--', linewidth=1.5, label='Zero Return Boundary')
    
    ax.set_title("Market Volatility Profile: Distribution of Apple Daily Returns", fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Daily Percentage Change (%)", fontsize=11)
    ax.set_ylabel("Frequency (Days)", fontsize=11)
    ax.legend(frameon=False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    return fig


def plot_monthly_volume(df: pd.DataFrame) -> plt.Figure:
    """
    Generates a bar chart tracking historical trading volume shifts across months.
    """
    fig, ax = plt.subplots(figsize=(14, 5))
    
    ax.bar(df['YearMonth'], df['Volume'], color='#34495e', alpha=0.9, width=0.7)
    
    ax.set_title("Investor Engagement: Average Trading Volume Across Timeline", fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Timeline (Year-Month)", fontsize=11)
    ax.set_ylabel("Average Volume (Shares Traded)", fontsize=11)
    
    # Prevent x-axis textual clutter
    plt.xticks(rotation=90, fontsize=7)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    return fig


def plot_volume_by_direction(df: pd.DataFrame) -> plt.Figure:
    """
    Generates a dual-category bar chart comparing trading volumes on positive vs negative days.
    """
    fig, ax = plt.subplots(figsize=(7, 5))
    
    # Standard premium finance color mapping: Crimson Red for Down, Emerald Green for Up
    colors = ['#c0392b', '#27ae60']
    
    bars = ax.bar(df['Direction'], df['Volume'], color=colors, width=0.4, edgecolor='#34495e', linewidth=1)
    
    # Add value labels on top of bars for executive clarity
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:,.0f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, fontweight='bold')

    ax.set_title("Market Psychology: Volume on Up Days vs Down Days", fontsize=14, fontweight='bold', pad=15)
    ax.set_ylabel("Average Shares Traded", fontsize=11)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    return fig