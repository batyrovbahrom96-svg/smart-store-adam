import os
import sqlite3
import pandas as pd
import pathlib

# Paths
DW_DIR = pathlib.Path("data/dw")
DB_PATH = DW_DIR / "smart_sales.db"
PREPARED = pathlib.Path("data/prepared")

DW_DIR.mkdir(parents=True, exist_ok=True)

# ----------------------------------------------------------
# 1. DELETE OLD DATABASE
# ----------------------------------------------------------
if DB_PATH.exists():
    DB_PATH.unlink()
    print("Old DW removed.")
else:
    print("No existing DW found.")

# ----------------------------------------------------------
# 2. CREATE SCHEMA MATCHING CSV EXACTLY
# ----------------------------------------------------------
def create_schema(cursor):

    cursor.execute("""
        CREATE TABLE customer (
            customer_id INTEGER PRIMARY KEY,
            name TEXT,
            region TEXT,
            join_date TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE product (
            ProductID INTEGER PRIMARY KEY,
            ProductName TEXT,
            Category TEXT,
            UnitPrice REAL,
            StockQuantity INTEGER,
            Supplier TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE sale (
            TransactionID INTEGER PRIMARY KEY,
            SaleDate TEXT,
            CustomerID INTEGER,
            ProductID INTEGER,
            StoreID INTEGER,
            CampaignID INTEGER,
            SaleAmount REAL,
            DiscountPercent REAL,
            PaymentType TEXT
        )
    """)

# ----------------------------------------------------------
# 3. INSERT FUNCTIONS (EXACT COLUMN ORDER)
# ----------------------------------------------------------
def insert_customers(df, cursor):
    cursor.executemany("""
        INSERT INTO customer (customer_id, name, region, join_date)
        VALUES (?, ?, ?, ?)
    """, df.values.tolist())


def insert_products(df, cursor):
    cursor.executemany("""
        INSERT INTO product (ProductID, ProductName, Category, UnitPrice, StockQuantity, Supplier)
        VALUES (?, ?, ?, ?, ?, ?)
    """, df.values.tolist())


def insert_sales(df, cursor):
    cursor.executemany("""
        INSERT INTO sale (
            TransactionID, SaleDate, CustomerID, ProductID, StoreID,
            CampaignID, SaleAmount, DiscountPercent, PaymentType
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, df.values.tolist())

# ----------------------------------------------------------
# 4. LOAD DATA
# ----------------------------------------------------------
def load_data():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("Creating schema...")
    create_schema(cursor)

    print("Loading CSV files...")
    customers = pd.read_csv(PREPARED / "customers_data_prepared.csv")
    products = pd.read_csv(PREPARED / "products_data_prepared.csv")
    sales = pd.read_csv(PREPARED / "sales_data_prepared.csv")

    print("Inserting customers...")
    insert_customers(customers, cursor)

    print("Inserting products...")
    insert_products(products, cursor)

    print("Inserting sales...")
    insert_sales(sales, cursor)

    conn.commit()
    conn.close()
    print("DW load complete. Success!")

# Run
if __name__ == "__main__":
    load_data()