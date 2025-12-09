import pandas as pd
import mysql.connector

df = pd.read_csv("data/processed/blinkit_transformed.csv")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root3107",
    database="blinkit_sales"
)

cursor = conn.cursor()

insert_query = """
INSERT INTO sales_data (
    item_fat_content, item_identifier, item_type,
    outlet_establishment_year, outlet_identifier,
    outlet_location_type, outlet_size, outlet_type,
    item_visibility, item_weight, total_sales,
    rating, outlet_age, sales_category
) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

for _, row in df.iterrows():
    cursor.execute(insert_query, tuple(row))

conn.commit()
conn.close()

print("✅ Data loaded successfully using Python!")
