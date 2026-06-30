import pandas as pd

#Load raw CSV
df = pd.read_csv(r"Data\Raw\06_industry_folio_count.csv")

#Remove duplicate rows
df = df.drop_duplicates()

#Remove extra spaces
df = df.apply(lambda col:col.str.strip() if col.dtype =="object" else col)

# Fill missing values
df = df.fillna("Unknown")

#SAved cleaned file
df.to_csv(r"Data\Processed\industry_folio_count_cleaned.csv", index=False)

print("industry_folio_count_cleaned.csv created_successfully!")