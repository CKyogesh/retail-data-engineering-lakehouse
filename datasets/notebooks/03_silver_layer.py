from pyspark.sql import SparkSession
from pyspark.sql.functions import *

from config.config import *

spark = SparkSession.builder.getOrCreate()

customers = spark.read.format("delta").load(
    BRONZE_PATH + "customers"
)

products = spark.read.format("delta").load(
    BRONZE_PATH + "products"
)

sales_a = spark.read.format("delta").load(
    BRONZE_PATH + "sales_company_a"
)

sales_b = spark.read.format("delta").load(
    BRONZE_PATH + "sales_company_b"
)

sales = sales_a.unionByName(sales_b)

customers = (
    customers
    .dropDuplicates(["customer_id"])
    .na.fill("Unknown")
)

products = (
    products
    .dropDuplicates(["product_id"])
)

sales = (
    sales
    .dropDuplicates(["order_id"])
)

customers.write.format("delta").mode("overwrite").save(
    SILVER_PATH + "customers"
)

products.write.format("delta").mode("overwrite").save(
    SILVER_PATH + "products"
)

sales.write.format("delta").mode("overwrite").save(
    SILVER_PATH + "sales"
)
