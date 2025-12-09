-- Revenue by Category
SELECT category, 
       SUM(total_sales) AS category_revenue
FROM sales_data
GROUP BY category
ORDER BY category_revenue DESC;

-- Top Selling Category by Quantity
SELECT category, 
       SUM(quantity) AS total_quantity
FROM sales_data
GROUP BY category
ORDER BY total_quantity DESC;
