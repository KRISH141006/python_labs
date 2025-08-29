import pandas as pd

s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])

vertical = pd.concat([s1, s2])
horizontal = pd.concat([s1, s2], axis=1)

print(vertical)
print(horizontal)
