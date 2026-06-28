from pyspark.sql import SparkSession
from pyspark.sql.types import *
import logging
from config.config import *

logging.basicConfig(level=logging.INFO)

spark = (
    SparkSession.builder
    .appName("Retail Data Ingestion")
    .getOrCreate()
)

customer_schema = StructType([
    StructField("customer_id", IntegerType(), False),
    StructField("first_name", StringType(), True),
    StructField("last_name", StringType(), True),
    StructField("city", StringType(), True),
    StructField("state", StringType(), True)
])

product_schema = StructType([
    StructField("product_id", StringType(), False),
    StructField("product_name", StringType(), True),
    StructField("category", StringType(), True),
    StructField("price", DoubleType(), True)
])

sales_schema = StructType([
    StructField("order_id", StringType(), False),
    StructField("customer_id", IntegerType(), False),
    StructField("product_id", StringType(), False),
    StructField("quantity", IntegerType(), True),
    StructField("sale_date", DateType(), True)
])

customers = spark.read.csv(
    RAW_PATH + CUSTOMERS,
    header=True,
    schema=customer_schema
)

products = spark.read.csv(
    RAW_PATH + PRODUCTS,
    header=True,
    schema=product_schema
)

sales_a = spark.read.csv(
    RAW_PATH + SALES_A,
    header=True,
    schema=sales_schema
)

sales_b = spark.read.csv(
    RAW_PATH + SALES_B,
    header=True,
    schema=sales_schema
)

logging.info(f"Customers: {customers.count()}")
logging.info(f"Products : {products.count()}")
logging.info(f"Sales A  : {sales_a.count()}")
logging.info(f"Sales B  : {sales_b.count()}")

customers.printSchema()
products.printSchema()
sales_a.printSchema()
