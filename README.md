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
## Task 3: Data Visualization & Dashboarding

### 🎯 Objective
Create professional data visualizations and an interactive executive dashboard.

### 🛠️ Tools Used
- Matplotlib, Seaborn — static visualizations
- Plotly — interactive visualizations
- Power BI Desktop — dashboard design and publishing

### 📁 Additional Files
```
├── notebooks/03_visualizations.ipynb        # All Python visualizations
├── dashboards/AMAZON SALES REPORT.pbix       # Power BI dashboard file
├── reports/monthly_sales_trend.png
├── reports/sales_by_category.png
├── reports/sales_vs_profit.png
├── reports/sales_distribution.png
├── reports/correlation_heatmap.png
├── reports/profit_boxen.png
├── reports/pairplot.png
├── reports/interactive_sales_by_category.html
├── reports/interactive_monthly_trend.html
```

### 📊 Visualizations Created
- Line chart: Monthly sales trend
- Bar chart: Total sales by category
- Scatter plot: Sales vs Profit
- Histogram: Sales distribution
- Heatmap: Correlation between Sales, Quantity, Discount, Profit, Shipping Cost
- Boxen plot: Profit distribution by category
- Pairplot: Relationships between key numeric variables
- Interactive Plotly charts (HTML): category sales and monthly trend

### 📈 Power BI Dashboard
Built an executive dashboard with KPI cards (total sales, customers, orders), sales trend line chart, category breakdown, geographic sales map, top 10 products/customers, and filter panel (date, region, category).

**Dashboard file:** [`dashboards/AMAZON SALES REPORT.pbix`](dashboards/AMAZON%20SALES%20REPORT.pbix)

### 💡 Key Insights
1. Sales distribution confirmed as heavily right-skewed, consistent with Task 1 findings.
2. Clear positive correlation between Sales and Profit, though with meaningful spread — some high-sales orders are still unprofitable due to discounting.
3. Category-level breakdown visually confirms Technology as the top-performing category by sales.

---

## Task 4: Advanced Analytics & Statistical Modeling

### 🎯 Objective
Apply statistical analysis, time series analysis, customer segmentation, and basic predictive modeling to extract deeper, data-driven insights.

### 🛠️ Tools Used
- `scipy.stats` — hypothesis testing, confidence intervals
- `statsmodels` — time series decomposition
- `scikit-learn` — K-Means clustering, PCA, Linear Regression

### 📁 Additional Files
```
├── notebooks/04_advanced_analytics.ipynb   # Full statistical + ML analysis
├── reports/time_series_decomposition.png
├── reports/moving_average_forecast.png
├── reports/elbow_method.png
├── reports/customer_clusters_pca.png
```

### 📊 Analysis Performed

**Statistical Analysis**
- Descriptive statistics (mean, median, mode, std dev, skewness) for Sales, Quantity, Discount, Profit, Shipping Cost
- Independent t-test: Profit (Consumer vs Corporate segment)
- Chi-square test: association between Region and Order Priority
- 95% confidence interval for mean Profit

**Time Series Analysis**
- Monthly resampling of Sales data
- Seasonal decomposition (trend, seasonality, residuals)
- 3-month moving average forecast

**Customer Segmentation (K-Means Clustering)**
- Feature engineering: total spend, order frequency, average order value, total profit per customer
- Standardized features and applied K-Means (K=4, selected via elbow method)
- 2D cluster visualization using PCA
- Profiled each segment by average behavior

**Predictive Modeling**
- Linear Regression predicting Sales from Quantity, Discount, and Shipping Cost
- 80/20 train/test split
- Evaluated using R², MAE, RMSE

### 💡 Key Insights

1. **No statistically significant profit difference between Consumer and Corporate segments** (t-test, p=0.848) — Consumer's higher *total* profit is driven by order volume, not higher per-order profitability.

2. **Region and Order Priority are significantly associated** (chi-square, p<0.001) — order urgency varies meaningfully by region, suggesting geographic factors influence fulfillment patterns.

3. **95% confidence interval for mean profit: ($27.10, $30.12)** — a statistically reliable estimate of true average profit per order.

4. **Sales show a consistent upward trend and strong annual seasonality**, with dips in Jan/Feb and peaks toward year-end (holiday season), confirmed via time series decomposition.

5. **Four distinct customer segments identified via K-Means clustering:**
   - **VIP Customers** (222 customers): highest spend and profit, frequent high-value orders — top retention priority
   - **Loyal Regulars** (552 customers): frequent buyers with moderate order values — dependable revenue base
   - **Occasional Big Spenders** (151 customers): infrequent but high-value orders — re-engagement opportunity
   - **Low-Value/New Customers** (665 customers): largest group by count, lowest spend/profit — growth opportunity

6. **Discount is the strongest predictor of Sales value** (Linear Regression coefficient: -56.25) — higher discounts are associated with lower sale values, reinforcing earlier findings that aggressive discounting hurts profitability. Model achieved R²=0.65 using just three features (Quantity, Discount, Shipping Cost).

### 🚀 How to Reproduce
```python
# Statistical tests
from scipy import stats
t_stat, p_value = stats.ttest_ind(consumer_profit, corporate_profit, equal_var=False)

# Time series decomposition
from statsmodels.tsa.seasonal import seasonal_decompose
decomposition = seasonal_decompose(ts_data, model='additive', period=12)

# Customer clustering
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
customer_features['Cluster'] = kmeans.fit_predict(X_scaled)

# Predictive model
from sklearn.linear_model import LinearRegression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
```
## Task 5: Final Report, Automation & Presentation

### 🎯 Objective
Create a final executive report, automate the data pipeline, and prepare the project for final submission.

### 🛠️ Tools Used
- ReportLab — PDF report generation
- GitHub Actions — pipeline scheduling and automation

### 📁 Additional Files
```
├── reports/executive_summary_report.pdf     # 2-page executive summary report
├── scripts/pipeline.py                      # Automated data pipeline script
├── .github/workflows/pipeline.yml           # GitHub Actions scheduling config
├── requirements.txt                         # Project dependencies
```

### 📄 Executive Summary Report
A 2-page PDF report summarizing the full project, including:
- Executive summary of the analysis and key business metrics
- Power BI dashboard screenshot
- Top 5 insights (drawn from Tasks 1–4)
- 3 actionable business recommendations with rationale

**Report:** [`reports/executive_summary_report.pdf`](reports/executive_summary_report.pdf)

### ⚙️ Automated Data Pipeline
Built a reusable Python pipeline (`scripts/pipeline.py`) that:
1. Loads raw data from CSV/Excel
2. Cleans it (removes junk columns, handles missing values, fixes data types)
3. Calculates key business KPIs (total sales, profit, orders, customers, average order value, profit margin, top category, top region)
4. Exports cleaned data and KPIs to a timestamped Excel file

Scheduled to run automatically via **GitHub Actions** (`.github/workflows/pipeline.yml`) on a daily cron schedule, with support for manual triggering.

### 📊 Sample Pipeline Output (KPIs)
| KPI | Value |
|---|---|
| Total Sales | $12,642,501.91 |
| Total Profit | $1,467,457.29 |
| Total Orders | 25,035 |
| Total Customers | 1,590 |
| Average Order Value | $246.49 |
| Average Profit Margin | 11.61% |
| Top Category | Technology |
| Top Region (by Profit) | Central |

### 🏷️ Final Release
This project is tagged as **`v1.0.0`**, representing the complete, final version of the ApexPlanet Data Analytics Internship deliverables across all 5 tasks.

### 🚀 How to Run the Pipeline
```bash
pip install -r requirements.txt
python scripts/pipeline.py
```

---

## 📌 Project Summary

This repository documents a complete, 5-task data analytics internship project at ApexPlanet Software Pvt. Ltd., covering the full analytics lifecycle on a global e-commerce sales dataset (51,290 orders, 2011–2014):

1. **Foundational Setup & EDA** — environment setup, data cleaning, exploratory analysis
2. **SQL for Data Extraction** — SQL fundamentals, advanced queries, Python-SQL integration
3. **Data Visualization & Dashboarding** — Python visualizations, interactive Power BI dashboard
4. **Advanced Analytics & Statistical Modeling** — hypothesis testing, time series analysis, clustering, predictive modeling
5. **Final Report, Automation & Presentation** — executive summary report, automated pipeline, final packaging

**Author:** Yelletiwar Rohan Reddy
**Internship:** Data Analytics, ApexPlanet Software Pvt. Ltd.
**Offer ID:** APSPL2645037
