import pandas as pd

df =pd.read_csv(r"Data\Raw\07_scheme_performance.csv")

df = df.drop_duplicates()

df = df.apply(lambda col:col.str.strip() if col.dtype =="object" else col)

# fill missing values
df = df.fillna("Unknown")

df.to_csv(r"Data\Processed\scheme_performance_cleaned.csv", index=False)

print("scheme_performance_cleaned.py created successfully!")