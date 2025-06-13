import pandas as pd
import math

# e 
df = pd.read_csv("sample_products.csv")

# t
df["unit_prince"] = df["unit_price"].apply(math.ceil)

# l
df.to_csv("output/cleaned_products.csv",index=False)