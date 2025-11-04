"""
DataScrubber Class
Reusable class for cleaning datasets before ETL.
"""

import pandas as pd

class DataScrubber:
    def __init__(self, df):
        """Initialize with a pandas DataFrame"""
        self.df = df

    def remove_duplicates(self):
        """Remove duplicate rows"""
        before = len(self.df)
        self.df.drop_duplicates(inplace=True)
        after = len(self.df)
        print(f"Removed {before - after} duplicates")
        return self

    def handle_missing(self):
        """Drop rows with missing values"""
        before = len(self.df)
        self.df.dropna(inplace=True)
        after = len(self.df)
        print(f"Removed {before - after} rows with missing values")
        return self

    def remove_outliers(self, column, min_val, max_val):
        """Remove rows where values in 'column' fall outside given range"""
        if column in self.df.columns:
            before = len(self.df)
            self.df = self.df[(self.df[column] >= min_val) & (self.df[column] <= max_val)]
            after = len(self.df)
            print(f"Removed {before - after} outliers from {column}")
        return self

    def get_cleaned_data(self):
        """Return cleaned DataFrame"""
        return self.df