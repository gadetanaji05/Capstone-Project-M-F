import pandas as pd 

df = pd.read_csv(r"Data\Raw\04_monthly_sip_inflows.csv")

df = df.drop_duplicates()
df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

df.to_csv(r"Data\Processed\monthly_sip_inflows_cleaned.csv", index=False)

print("monthly_sip_inflows_cleaned.csv created successfully")