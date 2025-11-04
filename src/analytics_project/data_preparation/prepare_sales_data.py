"""
Prepare Sales Data
Cleans sales_data.csv by removing only true duplicates and extreme outliers.
Keeps rows even if some optional columns are missing.
"""

import pandas as pd
import os
from analytics_project.data_scrubber import DataScrubber

RAW_PATH = "data/raw/sales_data.csv"
PREPARED_PATH = "data/prepared/sales_data_prepared.csv"

def prepare_sales():
    # Load data
    df = pd.read_csv(RAW_PATH)
    print(f"Raw records: {len(df)}")

    # Convert possible numeric columns safely
    numeric_cols = ["SaleAmount", "DiscountPercent"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Initialize scrubber
    scrubber = DataScrubber(df)
    scrubber.remove_duplicates()

    # Get cleaned data
    df = scrubber.get_cleaned_data()

    # Drop rows with missing SaleAmount only if it's required for analysis
    if "SaleAmount" in df.columns:
        before = len(df)
        df = df.dropna(subset=["SaleAmount"])
        print(f"Removed {before - len(df)} rows missing SaleAmount")

    # Fill missing optional numeric columns with 0 instead of dropping everything
    for col in numeric_cols:
        if col in df.columns:
            df[col].fillna(0, inplace=True)

    # Remove only extreme outliers
    if "SaleAmount" in df.columns:
        before = len(df)
        df = df[(df["SaleAmount"] >= 0) & (df["SaleAmount"] <= 10000)]
        print(f"Removed {before - len(df)} outliers from SaleAmount")

    # Save cleaned file
    os.makedirs(os.path.dirname(PREPARED_PATH), exist_ok=True)
    df.to_csv(PREPARED_PATH, index=False)

    print(f"Prepared records: {len(df)}")
    print("Sales data scrubbed and saved.")

if __name__ == "__main__":
    prepare_sales()