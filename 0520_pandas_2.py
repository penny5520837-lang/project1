import pandas as pd

products = ["Apple", "Banana", "Orange", "Mango", "Grape", "Guava"]
prices = [30, 20, 25, 60, 45, 35]
sales = [100, 150, 80, 60, 90, 54]

data_dict = {"Product": products, "Price": prices, "Sales": sales}
df_from_dict = pd.DataFrame(data_dict)


data_list = [
    ["Apple", 30, 100],
    ["Banana", 20, 150],
    ["Orange", 25, 80],
    ["Mango", 60, 60],
    ["Grape", 45, 90],
    ["Guava", 35, 54],
]
df = pd.DataFrame(data_list, columns=["Product", "Price", "Sales"])

print(df.head(5))
print(df.tail(5))


print(df.shape)

print(df.columns)


print(df.dtypes)


print(df.count())


summary_stats = df.describe().round(2)
print(summary_stats)

summary_stats.to_csv("0520_stock2.csv", index=True)