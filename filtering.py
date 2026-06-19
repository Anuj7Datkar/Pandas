# FIltering = keeping the rows that match a condition

import pandas as pd

df = pd.read_csv("pokemon.csv")

# tall_pokemon =df[df["Height"] >= 2]  #condition
#heavy_pokemon = df[df["Weight"] > 100] #condition
#legendary_pokemon = df[df["Legendary"] == 1] #condition
#water_pokemon = df[(df["Type1"] == "Water") |
#                   (df["Type2"] == "Water")]
fire_pokemon = df[(df["Type1"] == "Fire") &
                   (df["Type2"] == "Flying")]
print(fire_pokemon)