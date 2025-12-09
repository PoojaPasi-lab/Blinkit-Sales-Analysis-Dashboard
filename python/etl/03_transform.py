import pandas as pd
import datetime

input_file = "data/processed/blinkit_cleaned.csv"
output_file = "data/processed/blinkit_transformed.csv"

df = pd.read_csv(input_file)

# ✅ 1. Standardize item_fat_content
df['item_fat_content'] = df['item_fat_content'].replace({
    'LF': 'Low Fat',
    'low fat': 'Low Fat',
    'reg': 'Regular'
})

# ✅ 2. Handle missing item_weight safely
df['item_weight'] = df['item_weight'].fillna(df['item_weight'].mean())

# ✅ 3. Create Outlet Age
current_year = datetime.datetime.now().year
df['outlet_age'] = current_year - df['outlet_establishment_year']

# ✅ 4. SAFE Sales Category Using Quantiles (NO bin errors ever)
df['sales_category'] = pd.qcut(
    df['total_sales'],
    q=3,
    labels=['Low Sales', 'Medium Sales', 'High Sales']
)

# ✅ 5. Ensure rating is numeric
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# ✅ Save Transformed Data
df.to_csv(output_file, index=False)

print("✅ Data Transformed Successfully & Saved as blinkit_transformed.csv")
