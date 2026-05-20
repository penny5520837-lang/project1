import pandas as pd

# 1. 建立 Series
# 方法一：用 list 建立 stock1
stock1 = pd.Series([120, 80, None, 60, 95, None, 110])

# 方法二：自訂索引建立 stock2
stock2 = pd.Series(
    [120, 80, None, 60, 95, None, 110],
    index=["Apple", "Banana", "Orange", "Mango", "Grape", "Peach", "Melon"],
)

# 2. 用 to_dict() 轉成字典 stock3
stock3 = stock2.to_dict()

# --- 開始輸出結果 ---

print("stock1")
print(stock1)
print()

print("stock2")
print(stock2)
print()

print("stock3")
print(stock3)
print()

# 3. 取值方式 (取得 Banana 的庫存值)
print("Banana 庫存：", stock2["Banana"])
print()

# 4. 檢查缺失值 (使用 isnull() 與 isnull().sum())
print("缺失值檢查：")
print(stock2.isnull())
print()

print("缺失值數量：", stock2.isnull().sum())

# 5. 用 to_csv() 儲存檔案
# 注意：這裡不加 index=False，才能把 Apple, Banana 等水果索引一起存進去喔！
stock2.to_csv("0520_stock.csv")
print("存檔完成")