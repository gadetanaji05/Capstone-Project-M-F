import pandas as pd

# Load Dataset
df = pd.read_csv("Data/Raw/08_investor_transactions.csv")

# First 5 Rows
print(df.head())

# Column names
print("\nColumns:")
print(df.columns.tolist())

# Total records
print("\nTotal Records:",len(df))

# Convert transaction-date to datetime
df['transaction_date'] = pd.to_datetime(df["transaction_date"])

# check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# checked duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# check transaction types
print("\nTransaction types:")
print(df["transaction_type"].unique())

# check KYC status
print("\nKYC Status:")
print(df["kyc_status"].unique())

# Save cleaned data
df.to_csv("Data/Processed/investor_transactions_cleaned.csv",index=False)

print("\nCleaned file saved successfully!")
