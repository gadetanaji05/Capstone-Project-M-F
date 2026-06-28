import pandas as pd
from sqlalchemy import create_engine

# create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

print("Database created successfully!")

nav_df = pd.read_csv("Data/Processed/nav_history_cleaned.csv")
investor_df = pd.read_csv("Data/Processed/investor_transactions_cleaned.csv")

nav_df.to_sql("fact_nav", engine, if_exists="replace", index=False)
investor_df.to_sql("fact_transactions",engine,if_exists="replace",index=False)

print("Data loaded into SQLite successfully!")