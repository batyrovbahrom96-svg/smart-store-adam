import pandas as pd
import pathlib

RAW = pathlib.Path("data/raw/customers_data.csv")
OUT = pathlib.Path("data/prepared/customers_data_prepared.csv")

def prepare_customers():
    df = pd.read_csv(RAW)

    df = df.rename(columns={
        "CustomerID": "customer_id",
        "Name": "name",
        "Region": "region",
        "JoinDate": "join_date"
    })

    df = df[["customer_id", "name", "region", "join_date"]]

    df.to_csv(OUT, index=False)
    print("Customers prepared.")

if __name__ == "__main__":
    prepare_customers()