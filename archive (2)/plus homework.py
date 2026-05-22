import pandas as pd

# ============================================================
# 1. 讀取老年人原始資料集
# ============================================================
df = pd.read_csv('old.csv')

print("=" * 50)
print("【資料處理中】正在使用 Series 語法進行高齡者數據統計...")
print("=" * 50)

# ============================================================
# 2. 用 groupby 計算並取出 Series 數據（不轉成 DataFrame，保留為 Series 格式）
# ============================================================

# 【題目一】女性與男性的教育平均對比 (自訂索引為：Female, Male)
s_edu = df.groupby('Gender')['Education_Level'].mean().round(2)

# 【題目二】城鄉 ✕ 心理健康 (自訂多重索引為：Rural/Urban 與 Female/Male)
s_mental = df.groupby(['Region', 'Gender'])['GDS_Score'].mean().round(2)

# 【題目三】生活習慣 ✕ 睡眠品質 (自訂多重索引為：Smoking_Status 與 Alcohol_Use)
s_sleep = df.groupby(['Smoking_Status', 'Alcohol_Use'])['Sleep_Quality_Score'].mean().round(2)

# ============================================================
# 3. 仿照範例：用 to_dict() 轉成字典檢視
# ============================================================
print("--- 題目一的字典格式 (to_dict) ---")
print(s_edu.to_dict())
print()

# ============================================================
# 4. 仿照範例：取值方式 (取得都市女性 Urban Female 的憂鬱指數)
# ============================================================
print("都市女性 (Urban, Female) 的平均憂鬱指數：", s_mental["Urban", "Female"])
print()

# ============================================================
# 5. 仿照範例：檢查缺失值 (isnull() 與數量統計)
# ============================================================
print("該資料集『睡眠品質』Series 缺失值總數量：", df['Sleep_Quality_Score'].isnull().sum())
print()

# ============================================================
# 6. 用 to_csv() 儲存檔案
# 注意：這裡「不加 index=False」，才能把性別、城鄉等自訂索引一起存進去喔！
# ============================================================
output_filename = 'plushomework.CSV'

with open(output_filename, 'w', encoding='utf-8-sig') as f:
    f.write("=== 【題目一】女性與男性的教育平均對比 ===\n")
    s_edu.to_csv(f, index=True)  # 保留自訂索引
    f.write("\n")

    f.write("=== 【題目二】城鄉 ✕ 心理健康 (GDS憂鬱指數) 交叉統計 ===\n")
    s_mental.to_csv(f, index=True)  # 保留多重索引
    f.write("\n")

    f.write("=== 【題目三】生活習慣 (菸酒) ✕ 睡眠品質 交叉統計 ===\n")
    s_sleep.to_csv(f, index=True)  # 保留多重索引

print(f"🎉 存檔完成！已成功輸出至：{output_filename}")