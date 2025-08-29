# example-codes

# 1

import pandas as pd
data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print(series)

# 2

import pandas as pd
# Arithmetic Operations
series2 = series + 10
print(series2)
# Filtering
filtered_series = series[series > 2]
print(filtered_series)
# Statistical Calculations
mean_value = series.mean()
print(mean_value)

# 3

import pandas as pd
# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)

# 
print(df[['Name']])

# 
df['Salary'] = [70000, 80000, 90000]
print(df)

#

df = df.drop('City', axis=1)
print(df)

# 
# Return row 0:
print(df.loc[[0]])


# Return row 0 and 1:
# use a list of indexes:
print(df.loc[[0, 1]])

#
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)


# 4

import pandas as pd
dat = pd.read_csv("Exp_9_data.csv")
print(dat)

# 5

import pandas as pd
Biodata = {'Name': ['John', 'Emily', 'Mike', 'Lisa'],
        'Age': [28, 23, 35, 31],
        'Gender': ['M', 'F', 'M', 'F']
        }
df = pd.DataFrame(Biodata)
# Save the dataframe to a CSV file
df.to_csv('Biodata.csv', index=False)
print(pd.read_csv("Biodata.csv"))

# 6

import pandas as pd
dat = pd.read_csv("Biodata.csv")
print(dat.info())
# shows first and last five rows
print(dat.head())
print(dat.tail())
print(dat.describe())

# 7

import pandas as pd
dat = pd.read_csv("Exp_9_data.csv")
print(dat[['Name']])
print(dat[['Name','Number']])
print(dat.loc[[1]])

# 8

import pandas as pd
import numpy as np

data = {
    'A': [np.nan, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': np.random.normal(50, 15, 10),
    'C': np.random.rand(10) * 100,
    'D': np.linspace(1, 10, 10),
    'E': np.logspace(1, 2, 10)
}
df = pd.DataFrame(data)
print(df)