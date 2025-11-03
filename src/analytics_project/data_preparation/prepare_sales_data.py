"""
Prepare Sales Data
Cleans sales_data.csv by removing duplicates, missing values, and extreme amounts.
"""

import pandas as pd
import os

RAW_PATH = "data/raw/sales_data.csv"
PREPARED_PATH = "data/prepared/sales_data_prepared.csv"

def prepare_sales():
    df = pd.read_csv(RAW_PATH)
    print(f"Raw records: {len(df)}")

    # Remove duplicates and missing
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    # Remove unrealistic SaleAmount or DiscountPercent values
    if "SaleAmount" in df.columns:
        df = df[df["SaleAmount"] < 100000]
    if "DiscountPercent" in df.columns:
        df = df[df["DiscountPercent"] <= 80]

    os.makedirs(os.path.dirname(PREPARED_PATH), exist_ok=True)
    df.to_csv(PREPARED_PATH, index=False)
    print(f"Prepared records: {len(df)}")
    print("Sales data cleaned and saved.")

if __name__ == "__main__":
    prepare_sales()