import pandas as pd

# series =  A Pandas 1-Dimensional labeled array that can hold any data type 
#           its only a column in a spreadsheet (1-Dimensional)

data = [100, 102, 104,200,202]

series = pd.Series(data, index=["a","b","c","d","e"])
# series.loc["c"] = 200 # updating

#print(series.iloc[0])  #access using index

print(series[series < 200])  #accessing specific elements using condition