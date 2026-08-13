# ApexPlanet Data Analytics Internship — Task 1

## 📌 Project Overview
This project is part of my **Data Analytics Internship at ApexPlanet Software Pvt. Ltd.**
Task 1 focuses on foundational setup, data cleaning, and exploratory data analysis (EDA) on a global e-commerce sales dataset.

## 🎯 Objective
Set up a proper analytics environment, clean a real-world messy dataset, and extract meaningful business insights through exploratory analysis.

## 🗂️ Dataset
- **Name:** E-commerce Sales Dataset
- **Size:** 51,290 orders × 24 columns
- **Coverage:** Global orders across multiple markets (US, APAC, EU, Africa, and more)
- **Key fields:** Order Date, Ship Date, Category, Sub-Category, Sales, Quantity, Discount, Profit, Shipping Cost, Market, Region

## 🛠️ Tools & Libraries
- Python 3.11
- Jupyter Notebook
- pandas, numpy
- matplotlib, seaborn
- sqlalchemy

## 📁 Project Structure
```
apexplanet-data-analytics/
├── data/               # Raw and cleaned datasets
├── notebooks/          # Jupyter notebooks with EDA
├── scripts/            # Reusable Python scripts
├── reports/            # Summary reports
├── dashboards/         # Visualization dashboards
└── README.md
```

## 🧹 Data Cleaning Steps
1. Removed 232 empty/junk columns introduced during Excel → CSV conversion
2. Checked and confirmed no duplicate records
3. Converted `Order Date` and `Ship Date` from text to proper datetime format
4. Converted categorical columns (Ship Mode, Segment, Market, Region, Category, Sub-Category, Order Priority) to category dtype for efficiency
5. Identified and handled outliers in `Sales` and `Profit` using the IQR method

## 📊 Exploratory Data Analysis
- Distribution analysis of Sales (histogram, boxplot)
- Total Sales by Category (bar chart)
- Monthly Sales trend over time (line chart)
- Correlation heatmap across Sales, Quantity, Discount, Profit, and Shipping Cost

## 💡 Key Insights
1. **Postal Code is missing in ~80% of orders** — not a data quality issue, but a reflection of the dataset's global scope, since postal codes were only reliably captured for US-based orders.
2. **Some orders are highly unprofitable**, with Profit ranging from -6,599 to +8,399 — heavy discounting and high shipping costs can turn otherwise strong sales into losses.
3. **Sales are right-skewed**, with most orders falling in the low-to-mid value range and a small number of large orders pulling the average up — typical of retail/e-commerce data.
4. Outlier removal on Sales and Profit reduced the dataset by ~26.5%, showing a meaningful share of orders sit outside "typical" ranges — worth analyzing separately rather than discarding entirely.
5. Certain product categories consistently outperform others in total sales, highlighting where the business generates the most revenue.

## 🚀 How to Run
1. Clone this repository
2. Install dependencies:
   ```
   pip install pandas numpy matplotlib seaborn plotly sqlalchemy openpyxl
   ```
3. Open `notebooks/01_eda.ipynb` in Jupyter Notebook
4. Run all cells

## 👤 Author
**Yelletiwar Rohan Reddy**
Data Analytics Intern @ ApexPlanet Software Pvt. Ltd.
## Task 2: SQL for Data Extraction

### 🎯 Objective
Master SQL queries for data extraction and business analysis, and integrate SQL with Python for automated data workflows.

### 🛠️ Tools Used
- SQLite (via Python's built-in `sqlite3` module)
- `sqlalchemy` and `pandas.read_sql()` for Python-SQL integration

### 📁 Additional Files
```
├── data/ecommerce.db          # SQLite database (cleaned dataset loaded as 'orders' table)
├── notebooks/02_sql_extraction.ipynb   # SQL practice + business questions notebook
├── scripts/business_queries.sql        # All 10 business question queries
├── scripts/db_utils.py                 # Reusable database utility functions
```

### 🗃️ SQL Concepts Practiced
- SELECT, WHERE, ORDER BY, LIMIT
- GROUP BY, HAVING
- JOINs (with a custom region-manager lookup table)
- Subqueries and CTEs (`WITH` clause)
- Window functions: ROW_NUMBER, RANK, LAG
- Views for reusable queries

### 📊 10 Business Questions Answered
1. Top 5 products by sales (per category)
2. Monthly sales trend (with month-over-month change)
3. Customer segmentation by spend
4. Most profitable region
5. Shipping mode usage and average delivery time
6. Discount level impact on profit
7. Top 5 customers by profit generated
8. Most valuable customer segment
9. Order priority vs average profit
10. Year-over-year sales growth

### 💡 Key Insights
1. **Discounts above ~30% turn orders unprofitable on average** — at 85% discount, average profit drops to -$1,534 per order, making discount strategy a critical profitability lever.
2. **Central region generates the most profit** (~$311K), while Canada and Southeast Asia are barely profitable — a strong candidate for deeper regional strategy review.
3. **Consumer segment drives the most sales and profit**, ahead of Corporate and Home Office, suggesting marketing/retention efforts are well-placed there.
4. **Sales have grown consistently year-over-year**: +18.5% (2012), +27.2% (2013), +26.25% (2014).
5. **Order priority has minimal effect on profitability** — "Critical" orders aren't meaningfully more profitable than "Low" priority ones, suggesting priority labels don't currently reflect profit-driven decision-making.

### 🚀 How to Use the Database Utility
```python
from scripts.db_utils import run_query, get_top_n, get_summary_by_group

# Run any custom SQL query
result = run_query("SELECT * FROM orders LIMIT 10;")

# Get top N rows by a column
top_sales = get_top_n('orders', 'Sales', n=10)

# Get grouped summary
category_summary = get_summary_by_group('orders', 'Category', 'Sales')
```
