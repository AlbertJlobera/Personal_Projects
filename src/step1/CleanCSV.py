# Import pandas
import pandas as pd
# Import numpy
import numpy as np

# Load csv as df
df = pd.read_csv('df.items.csv')
# Drop nulls
df.dropna(inplace=True)
# Sort values by Price max to min to extract the fifth expensive products
df.sort_values(by=['Price'], ascending=False,inplace=True)
# Reset index
df.reset_index(drop=True,inplace=True)
# Create a new DataFrame with the fifth first products as five_products
five_products = df.head(5)
# Save CSV as products_ready.csv no index
five_products.to_csv('products_ready.csv',index=False)
