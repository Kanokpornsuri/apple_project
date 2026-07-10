import os
import matplotlib.pyplot as plt

# Import the functions we made inside the pipeline folder
from pipeline.load import load_raw
from pipeline.clean import clean
from pipeline.analyze import (
    analyze_price_trend,
    analyze_daily_returns,
    analyze_monthly_volume,
    analyze_volume_by_direction
)
from pipeline.visualize import (
    plot_price_trend,
    plot_daily_returns_distribution,
    plot_monthly_volume,
    plot_volume_by_direction
)

def main():
    # 1. Create outputs folder if it does not exist
    os.makedirs("outputs", exist_ok=True)
    
    # 2. Load the data
    print("Step 1: Loading Apple stock data...")
    raw_data = load_raw("data/apple.csv")
    
    # 3. Clean the data
    print("Step 2: Cleaning data and fixing dates...")
    cleaned_data = clean(raw_data)
    
    # 4. Run Analysis & Save Chart 1: Price History (Trend)
    print("Step 3: Analyzing price trend...")
    price_df = analyze_price_trend(cleaned_data)
    fig1 = plot_price_trend(price_df)
    fig1.savefig("outputs/1_price_trend.png")
    
    # 5. Run Analysis & Save Chart 2: Daily Jumps (Distribution)
    print("Step 4: Analyzing daily returns...")
    returns_df = analyze_daily_returns(cleaned_data)
    fig2 = plot_daily_returns_distribution(returns_df)
    fig2.savefig("outputs/2_daily_returns.png")
    
    # 6. Run Analysis & Save Chart 3: Monthly Volume (Groupby)
    print("Step 5: Analyzing monthly trading volume...")
    monthly_df = analyze_monthly_volume(cleaned_data)
    fig3 = plot_monthly_volume(monthly_df)
    fig3.savefig("outputs/3_monthly_volume.png")
    
    # 7. Run Analysis & Save Chart 4: Up vs Down Days (Comparison)
    print("Step 6: Comparing Up days vs Down days...")
    direction_df = analyze_volume_by_direction(cleaned_data)
    fig4 = plot_volume_by_direction(direction_df)
    fig4.savefig("outputs/4_market_direction.png")
    
    print("\n🎉 SUCCESS! All 4 charts are saved inside the 'outputs' folder!")

if __name__ == "__main__":
    main()