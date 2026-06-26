import os
import pandas as pd

folder_path = "Data/Raw"

for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(folder_path, file))

        print(f"\nFile: {file}")
        print("Shape:",df.shape)
        print("Data Types:")
        print(df.dtypes)
        print("First 5 Rows:")
        print(df.head())

        print("\Missing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())


