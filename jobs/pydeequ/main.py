from pyspark import __version__ as pyspark_version
from pyspark.sql import SparkSession, DataFrame, Column
from pyspark.sql.functions import col, left, length, lit
from pydeequ import __version__ as pydeequ_version

# ./environment/scripts/env.ps1; python ./jobs/pydeequ/main.py

spark = (
    SparkSession.builder
    # .config("spark.jars.packages", pydeequ.deequ_maven_coord)
    # .config("spark.jars.excludes", pydeequ.f2j_maven_coord)
    .master("local[*]")
    .appName("teste")
    .getOrCreate()
)

print(f"- pydeequ version: {pyspark_version}")
print(f"- pyspark version: {pydeequ_version}")

try:

    # Extracting dataset

    data: DataFrame = (
        spark.read.csv(
            path=".\datasets\csv\movies",
            inferSchema=True,
            header=True,
            sep=";",
            encoding="UTF-16",
        )
    )

    # Fixing Extra Caracter in Schema

    data: DataFrame = data.withColumnRenamed("CNPJ_DISTRIBUIDORA�", "CNPJ_DISTRIBUIDORA")

    # Fixing Extra Caracter in Column CNPJ_DISTRIBUIDORA

    col_cnpj_distribuidora_clean: Column = (
        left(
            col("CNPJ_DISTRIBUIDORA"),
            length(col("CNPJ_DISTRIBUIDORA")) - 1
        )
    )

    data: DataFrame = data.withColumn("CNPJ_DISTRIBUIDORA", col_cnpj_distribuidora_clean)

    # Outputs

    data.printSchema()
    data.show(n=1, vertical=True, truncate=False)

finally:
    spark.stop()