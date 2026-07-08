import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

print("Database created successfully!")

# Load cleaned CSV files
nav_df = pd.read_csv("Data/Processed/nav_history_cleaned.csv")
investor_df = pd.read_csv("Data/Processed/investor_transactions_cleaned.csv")
score_df = pd.read_csv("Notebooks/fund_scorecard.csv")

# Save to SQLite tables
nav_df.to_sql("fact_nav", engine, if_exists="replace", index=False)
investor_df.to_sql("fact_transactions", engine, if_exists="replace", index=False)
score_df.to_sql("fund_scorecard", engine, if_exists="replace", index=False)

print("Data loaded into SQLite successfully!")

# Verify tables
import sqlite3

conn = sqlite3.connect("bluestock_mf.db")

tables = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)

print("\nTables in Database:")
print(tables)

conn.close()