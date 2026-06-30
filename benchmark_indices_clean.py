import pandas as pd

df = pd.read_csv(r"Data\Raw\10_benchmark_indices.csv")

df=df.drop_duplicates()

df= df.apply(lambda col:col.str.strip() if col.dtype == "object" else col)

df = df.fillna("Unknown")

df.to_csv(r"Data\Processed\benchmark_indices_cleaned.csv",index=False)

print("benchmark_indices_cleaned.csv created successfully!")