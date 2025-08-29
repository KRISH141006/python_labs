import pandas as pd
import numpy as np

s1 = pd.Series([10, 20, 30])
s2 = pd.Series(np.array([1, 2, 3]))
s3 = pd.Series({'x': 100, 'y': 200})

print(s1)
print(s2)
print(s3)
