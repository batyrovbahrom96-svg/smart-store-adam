"""
Prepare Customers Data
Cleans customers_data.csv by removing duplicates, missing values, and outliers.
"""

import pandas as pd
import os

# Paths
RAW_PATH = "data/raw/customers_data.csv"
PREPARED_PATH = "data/prepared/customers_data_prepared.csv"

def prepare_customers():
    # Load data
    df = pd.read_csv(RAW_PATH)
    print(f"Raw records: {len(df)}")

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # Drop rows with missing values
    df.dropna(inplace=True)

    # Remove outliers for LoyaltyPoints (example: > 10000 points)
    if "LoyaltyPoints" in df.columns:
        df = df[df["LoyaltyPoints"] < 10000]

    # Save prepared file
    os.makedirs(os.path.dirname(PREPARED_PATH), exist_ok=True)
    df.to_csv(PREPARED_PATH, index=False)
    print(f"Prepared records: {len(df)}")
    print("Customers data cleaned and saved.")

if __name__ == "__main__":
    prepare_customers()