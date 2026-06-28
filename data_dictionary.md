# Data Dictionary

## fact_nav

| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | INTEGER | AMFI Code of Mutual Fund |
| date | DATE | NAV Date |
| nav | REAL | Net Asset Value |

## fact_transactions

| Column | Data Type | Description |
|--------|-----------|-------------|
| investor_id | INTEGER | Investor ID |
| transaction_date | DATE | Transaction Date |
| transaction_type | TEXT | SIP / Redemption / Lumpsum |
| amount_inr | REAL | Transaction Amount |
| kyc_status | TEXT | Verified / Pending |

## Source Files

- Data/Processed/nav_history_cleaned.csv
- Data/Processed/investor_transactions_cleaned.csv