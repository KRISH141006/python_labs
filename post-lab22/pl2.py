import pandas as pd

df = pd.read_csv("sample_data_1.csv")

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

print(df)
