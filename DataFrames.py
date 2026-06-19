import pandas as pd

# Dataframe = A tabular data structure with rows and columns. (2D)
#             Similar to an Excel spreadsheet

data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 50]
}

df = pd.DataFrame(data, index=["Employee1","Employee2","Employee3"])

#accessing elements
#print(df.loc["Employee1"])
#or
#print(df.iloc[0])

#add a new column
df["Job"]= ["Cook","N/A","Cashier"]

# add new rows
new_rows = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"},
                         {"Name": "Eugene", "Age": 60, "Job": "Manager"}], 
                       index=["Employee4", "Enployee5"])
df = pd.concat([df, new_rows])

print(df)