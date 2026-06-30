import pandas as pd

df = pd.read_csv(r"Data\Raw\03_aum_by_fund_house.csv")

df = df.drop_duplicates()

df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

df.to_csv(r"Data\Processed\aum_by_fund_house_cleaned.csv", index=False)

print("aum_by_fund_house_cleaned.csv created successfully")