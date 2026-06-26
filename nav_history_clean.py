import pandas as pd 

# Read NAV history CSV
df = pd.read_csv(r"Data\Raw\02_nav_history.csv")

# Display first 5 rows
print(df.head())

# Display column names
print(df.columns.tolist())

# Total records
print("Total Records:",len(df))

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by AMFI Code and Date
df = df.sort_values(by=["amfi_code","date"])

# display first 5 rows after sorting
print("\nAfter Sorting:")
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# check duplicate Records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Saved cleaned data
df.to_csv(r"Data\Processed\nav_history_cleaned.csv", index=False)

print("\nCleaned file saved successfully!")