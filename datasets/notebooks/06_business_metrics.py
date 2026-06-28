from pyspark.sql import SparkSession
from pyspark.sql.functions import *

from config.config import *

spark = SparkSession.builder.getOrCreate()

gold = spark.read.format("delta").load(
    GOLD_PATH + "sales_gold"
)

print("Revenue")

gold.agg(
    sum("sales_amount").alias("Total Revenue")
).show()

print("Revenue by State")

gold.groupBy("state") \
    .agg(
        sum("sales_amount").alias("Revenue")
    ) \
    .orderBy(desc("Revenue")) \
    .show()

print("Top Products")

gold.groupBy("product_name") \
    .agg(
        sum("sales_amount").alias("Revenue")
    ) \
    .orderBy(desc("Revenue")) \
    .show(10)

print("Top Customers")

gold.groupBy(
    "customer_id",
    "first_name",
    "last_name"
).agg(
    sum("sales_amount").alias("Revenue")
).orderBy(
    desc("Revenue")
).show(10)
