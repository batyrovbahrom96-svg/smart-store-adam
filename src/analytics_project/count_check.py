import pandas as pd

# Customers
raw_customers = pd.read_csv("data/raw/customers_data.csv")
prep_customers = pd.read_csv("data/prepared/customers_data_prepared.csv")
print("Customers:", len(raw_customers), "→", len(prep_customers))

# Products
raw_products = pd.read_csv("data/raw/products_data.csv")
prep_products = pd.read_csv("data/prepared/products_data_prepared.csv")
print("Products:", len(raw_products), "→", len(prep_products))

# Sales
raw_sales = pd.read_csv("data/raw/sales_data.csv")
prep_sales = pd.read_csv("data/prepared/sales_data_prepared.csv")
print("Sales:", len(raw_sales), "→", len(prep_sales))