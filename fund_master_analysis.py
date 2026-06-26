import pandas as pd

df = pd.read_csv(r"Data\Raw\01_fund_master.csv")
print(df.columns.tolist())

print("Total Records:",len(df))
print("\nUnique Fund Houses:")
print(df["fund_house"].nunique())

print("\nFund Houses:")
print(df["fund_house"].unique())

print("\nCategories:")
print(df["category"].unique())

print("\nSub Categories:")
print(df["sub_category"].unique())