from pyspark.sql import SparkSession
from delta import *

from config.config import *

spark = (
    SparkSession.builder
    .appName("Bronze Layer")
    .config(
        "spark.sql.extensions",
        "io.delta.sql.DeltaSparkSessionExtension"
    )
    .config(
        "spark.sql.catalog.spark_catalog",
        "org.apache.spark.sql.delta.catalog.DeltaCatalog"
    )
    .getOrCreate()
)

datasets = {
    "customers": CUSTOMERS,
    "products": PRODUCTS,
    "sales_company_a": SALES_A,
    "sales_company_b": SALES_B
}

for table, file in datasets.items():

    df = spark.read.option("header", True).csv(
        RAW_PATH + file
    )

    (
        df.write
        .format("delta")
        .mode("overwrite")
        .save(BRONZE_PATH + table)
    )

    print(f"{table} loaded to Bronze")
