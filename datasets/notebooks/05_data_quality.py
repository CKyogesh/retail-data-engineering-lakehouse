from pyspark.sql import SparkSession
from pyspark.sql.functions import *

from config.config import *

spark = SparkSession.builder.getOrCreate()

gold = spark.read.format("delta").load(
    GOLD_PATH + "sales_gold"
)

print("Row Count")
print(gold.count())

print("Duplicate Orders")

duplicates = (
    gold.groupBy("order_id")
    .count()
    .filter("count > 1")
)

duplicates.show()

print("Null Values")

gold.select([
    count(
        when(col(c).isNull(), c)
    ).alias(c)
    for c in gold.columns
]).show()
