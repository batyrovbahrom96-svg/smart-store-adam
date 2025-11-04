"""
Prepare Products Data
Cleans products_data.csv by removing duplicates, missing values, and outliers.
"""

import pandas as pd
import os

# File paths
RAW_PATH = "data/raw/products_data.csv"
PREPARED_PATH = "data/prepared/products_data_prepared.csv"

def prepare_products():
    # Load data
    df = pd.read_csv(RAW_PATH)
    print(f"Raw records: {len(df)}")

    # Drop duplicates and rows where all values are missing
    df.drop_duplicates(inplace=True)
    df.dropna(how='all', inplace=True)

    # Safely clean StockQuantity column
    if "StockQuantity" in df.columns:
        df["StockQuantity"] = pd.to_numeric(df["StockQuantity"], errors="coerce")
        # Only filter if there is at least one valid value
        if df["StockQuantity"].notna().sum() > 0:
            df = df[(df["StockQuantity"] >= 0) & (df["StockQuantity"] <= 10000)]

    # Save cleaned data
    os.makedirs(os.path.dirname(PREPARED_PATH), exist_ok=True)
    df.to_csv(PREPARED_PATH, index=False)
    print(f"Prepared records: {len(df)}")
    print("Products data cleaned and saved.")

if __name__ == "__main__":
    prepare_products()