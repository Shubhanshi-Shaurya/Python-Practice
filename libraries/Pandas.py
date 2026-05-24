import pandas as pd

df=pd.read_csv("currency.csv")
# print(df.head())
# print(df.tail())

#TRY TO READ FIRST 10,20,50 RECORDS
# print(df.head(10))
# print(df.head(20))
# print(df.head(50))

# print(df['Code'].dtype)
# print(df.dtypes)
# print(df.columns)
# print(df.axes)
# print(df.ndim)
# print(df.size)
# print(df.shape)
# print(df.values)

print(df.describe())
# print(df.max())
# print(df.min())
# print(df.mean())
# print(df.median())
# print(df.std())
print(df.sample(10))


