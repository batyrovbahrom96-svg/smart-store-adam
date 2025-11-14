
# SMART STORE ANALYTICS PROJECT
DATA WAREHOUSE IMPLEMENTATION (P4)

Overview
This project prepares, cleans, and loads sales data into a small data warehouse.
The goal is to support analysis, reporting, and business decisions.
The workflow follows five stages: design, build, load, verify, and document.

Business Goal
Help the store understand customers, products, and sales.
Support queries about revenue, regions, customer activity, and product demand.

Data Warehouse Schema
The warehouse uses a star schema.
One fact table: sale.
Two dimension tables: customer and product.

Table Definitions
customer
customer_id
name
region
join_date

product
product_id
product_name
category

sale
sale_id
customer_id
product_id
sale_amount
sale_date

ETL Process
The script etl_to_dw.py creates the schema, removes the old database, loads cleaned CSV files, and inserts all rows.
The ETL runs in three steps: create schema, delete old rows, insert new data.

Files Used
data/prepared/customers_data_prepared.csv
data/prepared/products_data_prepared.csv
data/prepared/sales_data_prepared.csv

Output
A complete SQLite DW file saved in data/dw/smart_sales.db.

How to Run
Activate the virtual environment.
Run the script from the project root:
python src/analytics_project/etl_to_dw.py

Verification
All tables load correctly.
Data types match the warehouse schema.
Foreign keys align with customer_id and product_id.
The database opens in SQLite Viewer with populated tables.

Challenges
Duplicate customer IDs caused integrity errors.
The solution was to clean the CSV and regenerate a unique list.
Column mismatches caused SQL errors.
The solution was to align schema and CSV names exactly.

Notes
This DW prepares the project for dashboard creation, KPIs, and analysis.
It follows best practices for a simple learning environment.
