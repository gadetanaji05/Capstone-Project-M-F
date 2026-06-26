import pandas as pd

df = pd.read_csv(r"Data\Raw\01_fund_master.csv")

print("Total Records:", len(df))
print("Missing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nAMFI Codes Missing:")
print(df["amfi_code"].isnull().sum())
