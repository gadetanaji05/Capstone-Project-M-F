import pandas as pd

#Load raw CSV
df = pd.read_csv(r"Data\Raw\05_category_inflows.csv")

#Remove duplicate rows
df = df.drop_duplicates()

#Remove extra spaces
df = df.apply(lambda col:col.str.strip() if col.dtype == "object" else col)

#fill missing values
df.to_csv(r"Data\Processed\category_inflowa_cleaned.csv", index=False)

print("category_inflows_cleaned.csv created successfully!")