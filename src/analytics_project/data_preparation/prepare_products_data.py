"""
Prepare Products Data
Cleans products_data.csv by removing duplicates, missing values, and unrealistic StockQuantity values.
"""

import pandas as pd
import os
from analytics_project.data_scrubber import DataScrubber

RAW_PATH = "data/raw/products_data.csv"
PREPARED_PATH = "data/prepared/products_data_prepared.csv"

def prepare_products():
    # Load data
    df = pd.read_csv(RAW_PATH)
    print(f"Raw records: {len(df)}")

    # Convert numeric column safely
    if "StockQuantity" in df.columns:
        df["StockQuantity"] = pd.to_numeric(df["StockQuantity"], errors="coerce")

    # Initialize scrubber
    scrubber = DataScrubber(df)
    scrubber.remove_duplicates()

    # Get cleaned DataFrame
    df = scrubber.get_cleaned_data()

    # Drop rows missing essential product info
    essential_cols = [col for col in df.columns if col in ["ProductID", "ProductName"]]
    before = len(df)
    df.dropna(subset=essential_cols, inplace=True)
    print(f"Removed {before - len(df)} rows missing essential data")

    # Fill missing numeric StockQuantity with 0
    if "StockQuantity" in df.columns:
        df.fillna({"StockQuantity": 0}, inplace=True)

    # Remove unrealistic stock values (less than 0 or greater than 10,000)
    if "StockQuantity" in df.columns:
        before = len(df)
        df = df[(df["StockQuantity"] >= 0) & (df["StockQuantity"] <= 10000)]
        print(f"Removed {before - len(df)} outliers from StockQuantity")

    # Save cleaned dataset
    os.makedirs(os.path.dirname(PREPARED_PATH), exist_ok=True)
    df.to_csv(PREPARED_PATH, index=False)

    print(f"Prepared records: {len(df)}")
    print("Products data scrubbed and saved.")

if __name__ == "__main__":
    prepare_products()