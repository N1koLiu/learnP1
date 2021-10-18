import pandas as pd
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj1 = pd.Series(sdata)
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj2 = pd.Series(sdata, index=states)
obj3 = pd.isnull(obj2)

d = {'1': 'Alice','2': 'Bob','3': 'Rita','4': 'Molly','5': 'Ryan'}
S = pd.Series(d)

data = {"gre": [1, 2, 3, 4, 5], "toefl": [115, 104, 106, 100, 107]}
df = pd.DataFrame(data, index=[1, 2, 3, 4, 5])

df.where(df["toefl"]>105).dropna()
print(df)

