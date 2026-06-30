import pandas as pd

df = pd.read_csv(r"Data\Raw\09_portfolio_holdings.csv")

df = df.drop_duplicates()

df = df.apply(lambda col:col.str.strip() if col.dtype == "Object" else col)

df = df.fillna("Unknown")

df.to_csv(r"Data\Processed\portfolio_holdings_cleaned.csv",index=False)

print("Portfolio_holdings_cleaned.csv created successfully")