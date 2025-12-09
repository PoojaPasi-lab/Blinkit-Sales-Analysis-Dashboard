import pandas as pd
import os

# Paths
input_file = "data/raw/BlinkIT_raw.csv"
output_file = "data/raw/blinkit_raw_copy.csv"

# Create directory if not exists
os.makedirs("data/raw", exist_ok=True)

# ✅ Read CSV (NOT Excel)
df = pd.read_csv(input_file)

# Save as CSV
df.to_csv(output_file, index=False)

print("✅ Data Ingested Successfully & Saved as blinkit_raw.csv")
