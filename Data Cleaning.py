# Data Cleaning = the process of fixing/removing:
#                 incomplete, incorrect, or irrelevant data.
#                 ~75% of work done with Pandas is data cleaning

import pandas as pd

df = pd.read_csv("pokemon.csv")

# 1. Drop irrelevant columns
#df = df.drop(columns=["Legendary", "No"])

# 2. Handle missing columns
#df = df.dropna(subset=["Type2"])  #dropna=drop not available
#df= df.fillna({"Type2": "None"})

# 3. Fix inconsistent values
#df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
#                                   "Fire": "FIRE",
#                                   "Water": "WATER"})

# 4. standardize text
#df["Name"] = df["Name"].str.lower()

# 5. Fix data types
#df["Legendary"] = df["Legendary"].astype(bool)

# 6. remove duplicate values
df = df.drop_duplicates()

print(df.to_string())