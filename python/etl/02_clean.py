import pandas as pd
import os

input_file = "data/raw/blinkit_raw.csv"
output_file = "data/processed/blinkit_cleaned.csv"

os.makedirs("data/processed", exist_ok=True)

df = pd.read_csv(input_file)

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df.fillna(0, inplace=True)

# Save cleaned data
df.to_csv(output_file, index=False)

print("✅ Data Cleaned Successfully")
