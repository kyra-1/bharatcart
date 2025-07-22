# pyspark_jobs/funnel_analysis.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, when
import os
# 🚀 Start Spark
from utils.spark_session import get_spark
spark = get_spark("Funnel Analysis")



# 📥 Load Data
events_df = spark.read.csv("D:\cyber\pyspark\generator\data\events.csv", header=True, inferSchema=True)

# ✅ Basic Cleaning
events_df = events_df.select("user_id", "product_id", "event_type", "timestamp", "category", "city")

# 🧮 Funnel Counts
funnel_counts = events_df.groupBy("event_type").agg(count("*").alias("count")).orderBy("count", ascending=False)

print("🔍 Funnel Stage Breakdown:")
funnel_counts.show()

# 📊 Conversion per Category
from pyspark.sql.functions import lit  # already imported count, col

category_funnel = events_df.groupBy("category") \
    .pivot("event_type", ["view", "cart", "buy", "return"]) \
    .agg(count("event_type")) \
    .fillna(0)
# category_funnel = events_df.groupBy("category").pivot("event_type").agg(count("*")).fillna(0)
# Add Conversion Ratios
category_funnel = category_funnel.withColumn("view_to_cart", col("cart") / col("view")) \
                                 .withColumn("cart_to_buy", col("buy") / col("cart")) \
                                 .withColumn("buy_to_return", col("return") / col("buy"))

print("📈 Funnel by Category:")
category_funnel.orderBy("view", ascending=False).show(truncate=False)

# 📍 Conversion per City (optional)
city_funnel = events_df.groupBy("city") \
    .pivot("event_type", ["view", "cart", "buy", "return"]) \
    .agg(count("event_type")) \
    .fillna(0)

city_funnel = city_funnel.withColumn("view_to_buy", col("buy") / col("view"))

print("🏙️ Funnel by City:")
city_funnel.orderBy("view", ascending=False).show(10, truncate=False)

# 📤 Export basic funnel counts to CSV
funnel_counts_pd = funnel_counts.toPandas()
os.makedirs("output/funnel_analysis", exist_ok=True)
funnel_counts_pd.to_csv("output/funnel_analysis/funnel_metrics.csv", index=False)

# ✅ Final log
print("✅ Funnel data exported to output/funnel_analysis/funnel_metrics.csv")




# ✅ Stop Spark
spark.stop()
