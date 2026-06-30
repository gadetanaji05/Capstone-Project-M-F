import pandas as pd

df = pd.read_csv(r"Data\Raw\01_fund_master.csv")

df = df.drop_duplicates()
df = df.apply(lambda  col:col.str.strip() if
              col.dtype == "object" else col)

df["launch_date"] = pd.to_datetime(df["launch_date"],
                                   errors="coerce")
df.to_csv(r"Data\Processed\fund_master_cleaned.csv", index=False)

print("fund_master_cleaned.csv created successfully")