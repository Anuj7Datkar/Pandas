import pandas as pd

df = pd.read_csv("pokemon.csv")
df = pd.read_json("pokemon1.json")

print(df.to_string())