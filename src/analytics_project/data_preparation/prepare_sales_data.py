"""
Prepare Sales Data
Cleans sales_data.csv by removing duplicates, missing values, and outliers.
"""

import pandas as pd
import os

RAW_PATH = "data/raw/sales_data.csv"
PREPARED_PATH = "data/prepared/sales_data_prepared.csv"

def prepare_sales():
    # Load raw data
    df = pd.read_csv(RAW_PATH)
    print(f"Raw records: {len(df)}")

    # Remove duplicates and rows where all values are missing
    df.drop_duplicates(inplace=True)
    df.dropna(how='all', inplace=True)

    # Safely clean SaleAmount
    if "SaleAmount" in df.columns:
        df["SaleAmount"] = pd.to_numeric(df["SaleAmount"], errors="coerce")
        if df["SaleAmount"].notna().sum() > 0:
            df = df[(df["SaleAmount"] > 0) & (df["SaleAmount"] < 10000)]

    # Safely clean DiscountPercent
    if "DiscountPercent" in df.columns:
        df["DiscountPercent"] = pd.to_numeric(df["DiscountPercent"], errors="coerce")
        if df["DiscountPercent"].notna().sum() > 0:
            df = df[(df["DiscountPercent"] >= 0) & (df["DiscountPercent"] <= 100)]

    # Save prepared data
    os.makedirs(os.path.dirname(PREPARED_PATH), exist_ok=True)
    df.to_csv(PREPARED_PATH, index=False)
    print(f"Prepared records: {len(df)}")
    print("Sales data cleaned and saved.")

if __name__ == "__main__":
    prepare_sales()