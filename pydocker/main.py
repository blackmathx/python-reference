import pandas as pd
import numpy as np


# Read the CSV file
df = pd.read_csv('data.csv')

# Show basic info
print(f"Rows: {len(df)}")
print(f"Columns: {list(df.columns)}")
print("\nFirst 5 rows:")
print(df.head())
