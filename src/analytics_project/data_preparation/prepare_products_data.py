"""
Prepare Products Data
Cleans products_data.csv by removing duplicates, missing values, and extreme values.
"""

import pandas as pd
import os

RAW_PATH = "data/raw/products_data.csv"
PREPARED_PATH = "data/prepared/products_data_prepared.csv"

def prepare_products():
    df = pd.read_csv(RAW_PATH)
    print(f"Raw records: {len(df)}")

    # Remove duplicates and missing
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    # Remove unrealistic stock quantities (example: > 5000)
    if "StockQuantity" in df.columns:
        df = df[df["StockQuantity"] < 5000]

    os.makedirs(os.path.dirname(PREPARED_PATH), exist_ok=True)
    df.to_csv(PREPARED_PATH, index=False)
    print(f"Prepared records: {len(df)}")
    print("Products data cleaned and saved.")

if __name__ == "__main__":
    prepare_products()