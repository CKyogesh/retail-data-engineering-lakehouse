from pyspark.sql import SparkSession
from pyspark.sql.functions import *

from config.config import *

spark = SparkSession.builder.getOrCreate()

customers = spark.read.format("delta").load(
    SILVER_PATH + "customers"
)

products = spark.read.format("delta").load(
    SILVER_PATH + "products"
)

sales = spark.read.format("delta").load(
    SILVER_PATH + "sales"
)

gold = (
    sales
    .join(customers, "customer_id")
    .join(products, "product_id")
)

gold = gold.withColumn(
    "sales_amount",
    col("quantity") * col("price")
)

gold.write.format("delta").mode("overwrite").save(
    GOLD_PATH + "sales_gold"
)
