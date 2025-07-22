# utils/spark_session.py
from pyspark.sql import SparkSession

def get_spark(app_name="BharatCart App"):
    return SparkSession.builder \
        .appName(app_name) \
        .getOrCreate()
