CREATE DATABASE IF NOT EXISTS blinkit_sales;
USE blinkit_sales;

CREATE TABLE sales_data (
    item_fat_content VARCHAR(50),
    item_identifier VARCHAR(50),
    item_type VARCHAR(100),
    outlet_establishment_year INT,
    outlet_identifier VARCHAR(50),
    outlet_location_type VARCHAR(50),
    outlet_size VARCHAR(50),
    outlet_type VARCHAR(50),
    item_visibility FLOAT,
    item_weight FLOAT,
    total_sales FLOAT,
    rating FLOAT,
    outlet_age INT,
    sales_category VARCHAR(50)
);
SELECT COUNT(*) FROM sales_data;
SELECT * FROM sales_data LIMIT 5;