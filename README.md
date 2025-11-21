FINAL README.md FOR SUBMISSION
Cross-Platform Reporting with Power BI
Operating System

Windows 11

Tool

Power BI Desktop

Project Summary

The goal of this reporting project was to connect to the data warehouse created in P4 and perform core OLAP operations, including slicing, dicing, and drilldown. All analysis and visualizations were completed in Power BI Desktop.

SQL and Data Model

The dataset was imported from the data warehouse using ODBC.
Tables used: customer, product, sale.

Model View confirms all tables and relationships.

OLAP Operations Completed
1. Slice

I created a bar chart with:

X axis: SaleDate

Y axis: SaleAmount

Then I applied one filter (Count of SaleDate < 10) to isolate a small slice of the dataset.

Why:
A slice focuses on one dimension and gives a narrow view for quick analysis.

2. Dice

I created a column chart with:

X axis: ProductID

Y axis: Sum of SaleAmount

Two filters were added:

PaymentType = one value

StoreID = one value

Why:
A dice operation uses two dimensions to create a more specific subset of the data.

3. Drilldown

I created a line chart with:

X axis hierarchy: StoreID → ProductID

Y axis: Sum of SaleAmount

Drill mode was enabled, allowing movement from store-level to product-level details.

Why:
Drilldown lets the user move from general information to more detailed insights.

Challenges

Date column stored as text

Limited fields suitable for date-hierarchy drilldown

Solutions

Used numeric hierarchy StoreID → ProductID instead

Applied simple numeric filters to complete slice and dice

Most Interesting

Creating drilldown from two non-date fields

Managing OLAP operations using only basic columns

Would Explore Further

Date dimension tables

DAX calculations

Advanced Power BI transformations

Screenshots

Include the following screenshots in Canvas:

Model View

Slice visual

Dice visual

Drilldown visual
