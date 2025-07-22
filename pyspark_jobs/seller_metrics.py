# pyspark_jobs/seller_metrics.py
import os
os.environ["HADOOP_HOME"] = "C:/hadoop"

from utils.spark_session import get_spark
from pyspark.sql.functions import col, sum as _sum, count, round, lit

# 🛠️ Spark Init
# 🛠️ Spark Init
spark = get_spark("Seller Performance Metrics")

# 🔧 Fix native I/O error on Windows (disable native commit protocol)
spark._jsc.hadoopConfiguration().set("fs.file.impl", "org.apache.hadoop.fs.LocalFileSystem")
spark.conf.set("spark.sql.sources.commitProtocolClass",
               "org.apache.spark.sql.execution.datasources.SQLHadoopMapReduceCommitProtocol")



# 📥 Load data
events = spark.read.csv("D:\cyber\pyspark\generator\data\events.csv", header=True, inferSchema=True)
products = spark.read.csv("D:\cyber\pyspark\generator\data\products.csv", header=True, inferSchema=True)

# 🧮 Join with prices
merged = events.join(products.select("product_id", "price"), on="product_id", how="left")

# 💳 Filter buy and return events
buys = merged.filter(col("event_type") == "buy")
returns = merged.filter(col("event_type") == "return")

# 💰 Seller revenue = sum(price)
revenue_df = buys.groupBy("seller_id").agg(
    _sum("price").alias("total_revenue"),
    count(lit(1)).alias("total_orders")   # ✅ fixed
)

# 🔁 Return count
return_df = returns.groupBy("seller_id").agg(
    count(lit(1)).alias("total_returns")  # ✅ fixed
)

# 📊 Combine and compute return rate
final_df = revenue_df.join(return_df, on="seller_id", how="left") \
                     .fillna(0) \
                     .withColumn("return_rate", round(col("total_returns") / col("total_orders"), 2))

# 🥇 Top sellers
print("💼 Top 10 Sellers by Revenue:")
final_df.orderBy("total_revenue", ascending=False).show(10, truncate=False)

# 💾 Save output
final_df.coalesce(1).write.mode("overwrite").csv("output/seller_metrics", header=True)

# 🧹 Done
spark.stop()
