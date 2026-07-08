import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("bluestock_mf.db")

# Load fund scorecard table
score_df = pd.read_sql("SELECT * FROM fund_scorecard", conn)

# Ask user for risk level
risk = input("Enter Risk Level (Low/Moderate/High): ").strip().lower()

# Recommend top 3 funds
if risk == "low":
    result = score_df.sort_values(by="sharpe_ratio", ascending=False).head(3)

elif risk == "moderate":
    result = score_df.sort_values(by="score", ascending=False).head(3)

elif risk == "high":
    result = score_df.sort_values(by="alpha", ascending=False).head(3)

else:
    print("Invalid Risk Level!")
    conn.close()
    exit()

print("\nTop 3 Recommended Funds:\n")

print(result[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
        "risk_grade",
        "score",
        "sharpe_ratio",
        "alpha"
    ]
])

conn.close()