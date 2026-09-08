from pyspark.sql import SparkSession

# ./enviroment/scripts/env.ps1; python ./jobs/dummy_job/main.py

spark = (
    SparkSession.builder
    .master("local[*]")
    .appName("teste")
    .getOrCreate()
)

spark.range(5).show()

