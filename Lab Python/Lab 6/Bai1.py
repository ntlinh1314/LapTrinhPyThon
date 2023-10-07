import pandas as pd
df = pd.read_csv("Automobile_data.csv")
print(df)

print(df.head(6))

print(df.tail(7))

df1 = df [['company','price']][df.price == df['price'].max()]
print(df1)

xe = df.groupby('company')
mec = xe.get_group('mercedes-benz')
print(mec)

print(df['company'].value_counts())

gia = xe[['company','price']].mean('price')
print(gia)