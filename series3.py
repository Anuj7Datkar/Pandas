import pandas as pd

pokemon = {"Bulbasaur": 1, "Ivysaur": 2, "Venusaur": 3, "Charmander": 4, "Charmaleon": 5, "Charizard":6 }

series = pd.Series(pokemon)

print(series)