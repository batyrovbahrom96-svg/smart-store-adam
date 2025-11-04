"""
Prepare Customers Data
Cleans customers_data.csv by removing duplicates, minimal missing values, and unrealistic LoyaltyPoints.
"""

import pandas as pd
import os
from analytics_project.data_scrubber import DataScrubber

RAW_PATH = "data/raw/customers_data.csv"
PREPARED_PATH = "data/prepared/customers_data_prepared.csv"

def prepare_customers():
    # Load data
    df = pd.read_csv(RAW_PATH)
    print(f"Raw records: {len(df)}")

    # Convert numeric column safely
    if "LoyaltyPoints" in df.columns:
        df["LoyaltyPoints"] = pd.to_numeric(df["LoyaltyPoints"], errors="coerce")

    # Initialize scrubber and remove duplicates
    scrubber = DataScrubber(df)
    scrubber.remove_duplicates()

    # Get cleaned DataFrame
    df = scrubber.get_cleaned_data()

    # Drop rows missing critical info (like CustomerID or Name)
    essential_cols = [col for col in df.columns if col in ["CustomerID", "CustomerName"]]
    before = len(df)
    df.dropna(subset=essential_cols, inplace=True)
    print(f"Removed {before - len(df)} rows missing essential data")

    # Fill missing numeric LoyaltyPoints with 0
    if "LoyaltyPoints" in df.columns:
        df.fillna({"LoyaltyPoints": 0}, inplace=True)

    # Remove unrealistic outliers for LoyaltyPoints
    if "LoyaltyPoints" in df.columns:
        before = len(df)
        df = df[(df["LoyaltyPoints"] >= 0) & (df["LoyaltyPoints"] <= 10000)]
        print(f"Removed {before - len(df)} outliers from LoyaltyPoints")

    # Save cleaned dataset
    os.makedirs(os.path.dirname(PREPARED_PATH), exist_ok=True)
    df.to_csv(PREPARED_PATH, index=False)

    print(f"Prepared records: {len(df)}")
    print("Customers data scrubbed and saved.")

if __name__ == "__main__":
    prepare_customers()