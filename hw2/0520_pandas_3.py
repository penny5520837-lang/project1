import pandas as pd


df = pd.read_csv("pandashw.csv")


print("資料筆數：", df.shape)
print(df.head())


df_filter = df[(df["Branch"] == "Alex") & (df["Customer type"] == "Member")]
print("\n篩選後資料：")
print(df_filter.head())


group_class = df.groupby("Product line").agg({
    "Sales": "sum",
    "Rating": "mean"
}).reset_index()
c = group_class.round(2)

print("\n各產品線銷售與評分彙總：")
print(c)


group_count = df.groupby(["City", "Gender"]).agg({
    "Sales": "mean",
    "Invoice ID": "count"
}).reset_index()

group_count = group_count.round(2)
print("\n各城市與性別的平均銷售額與交易筆數：")
print(group_count)


top_product = c.loc[c["Sales"].idxmax()]
print("\n總銷售額最高的產品線：")
print(f"產品線名稱: {top_product['Product line']}")
print(f"總銷售金額: {top_product['Sales']}")
print(f"顧客平均評分: {top_product['Rating']}")


c["Sales"] = c["Sales"].map(lambda x: f"{x:.2f}")
c["Rating"] = c["Rating"].map(lambda x: f"{x:.2f}")

c.to_csv("0520_pandas_3OK.CSV", index=False, encoding="utf-8-sig")
