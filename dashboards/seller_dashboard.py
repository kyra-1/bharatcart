# dashboards/seller_dashboard.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 📂 Load processed seller metrics (output from PySpark job)
path = "D:\cyber\pyspark\pyspark_jobs\output\seller_metrics/"
latest_file = [f for f in os.listdir(path) if f.endswith(".csv")][0]
df = pd.read_csv(os.path.join(path, latest_file))

# 🧼 Sort and clean
sorted_df = df.sort_values("total_revenue", ascending=False).head(10)

# 🎨 Style
sns.set(style="whitegrid")

# 📊 Plot: Top 10 Sellers by Revenue
plt.figure(figsize=(12, 6))
sns.barplot(data=sorted_df, x="seller_id", y="total_revenue", palette="Blues_d")
plt.xticks(rotation=45, ha="right")
plt.title("Top 10 Sellers by Revenue")
plt.ylabel("Revenue")
plt.xlabel("Seller ID")
plt.tight_layout()
plt.savefig("../output/visuals/top_sellers_by_revenue.png")
plt.close()

# 📊 Plot: Return Rates for Top 10 Sellers
plt.figure(figsize=(12, 6))
sns.barplot(data=sorted_df, x="seller_id", y="return_rate", palette="Reds")
plt.xticks(rotation=45, ha="right")
plt.title("Return Rates for Top 10 Sellers")
plt.ylabel("Return Rate")
plt.xlabel("Seller ID")
plt.tight_layout()
plt.savefig("../output/visuals/return_rates.png")
plt.close()

print("✅ Seller dashboards saved to output/visuals/")
