#day 7
import pandas as pd
import numpy as np 

s = pd.Series([1,3,6,np.nan,44,1])
# print(s)

dates = pd.date_range('20180101', periods=6)
# print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['a','b','c','d'])
# print(df)

df1 = pd.DataFrame(np.arange(12).reshape(3,4))
print(df1.index)
print(df1.columns)