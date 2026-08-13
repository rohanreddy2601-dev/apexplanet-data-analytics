-- Task 2: SQL for Data Extraction - Business Questions
-- ApexPlanet Data Analytics Internship

-- Q1: Top 5 products by sales (per category)
WITH ranked AS (
    SELECT Category, "Product Name", SUM(Sales) AS total_sales,
           RANK() OVER (PARTITION BY Category ORDER BY SUM(Sales) DESC) AS product_rank
    FROM orders
    GROUP BY Category, "Product Name"
)
SELECT * FROM ranked WHERE product_rank <= 5 ORDER BY Category, product_rank;

-- Q2: Monthly sales trend
WITH monthly_sales AS (
    SELECT strftime('%Y-%m', "Order Date") AS month, SUM(Sales) AS total_sales
    FROM orders GROUP BY month
)
SELECT month, total_sales,
       LAG(total_sales) OVER (ORDER BY month) AS prev_month_sales,
       total_sales - LAG(total_sales) OVER (ORDER BY month) AS change
FROM monthly_sales ORDER BY month;

-- Q3: Customer segmentation by spend
SELECT "Customer Name", SUM(Sales) AS total_spend, COUNT(*) AS num_orders
FROM orders GROUP BY "Customer Name" ORDER BY total_spend DESC LIMIT 10;

-- Q4: Most profitable region
SELECT Region, SUM(Profit) AS total_profit
FROM orders GROUP BY Region ORDER BY total_profit DESC;

-- Q5: Shipping mode usage and average delivery time
SELECT "Ship Mode", COUNT(*) AS num_orders,
       AVG(julianday("Ship Date") - julianday("Order Date")) AS avg_days_to_ship
FROM orders GROUP BY "Ship Mode" ORDER BY num_orders DESC;

-- Q6: Discount level impact on profit
SELECT Discount, AVG(Profit) AS avg_profit, COUNT(*) AS num_orders
FROM orders GROUP BY Discount ORDER BY Discount;

-- Q7: Top 5 customers by profit
SELECT "Customer Name", SUM(Profit) AS total_profit
FROM orders GROUP BY "Customer Name" ORDER BY total_profit DESC LIMIT 5;

-- Q8: Most valuable customer segment
SELECT Segment, SUM(Sales) AS total_sales, SUM(Profit) AS total_profit, COUNT(*) AS num_orders
FROM orders GROUP BY Segment ORDER BY total_profit DESC;

-- Q9: Order priority vs average profit
SELECT "Order Priority", AVG(Profit) AS avg_profit, COUNT(*) AS num_orders
FROM orders GROUP BY "Order Priority" ORDER BY avg_profit DESC;

-- Q10: Year-over-year sales growth
WITH yearly_sales AS (
    SELECT strftime('%Y', "Order Date") AS year, SUM(Sales) AS total_sales
    FROM orders GROUP BY year
)
SELECT year, total_sales,
       LAG(total_sales) OVER (ORDER BY year) AS prev_year_sales,
       ROUND((total_sales - LAG(total_sales) OVER (ORDER BY year)) / LAG(total_sales) OVER (ORDER BY year) * 100, 2) AS growth_pct
FROM yearly_sales ORDER BY year;