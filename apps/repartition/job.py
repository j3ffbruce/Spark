from pyspark.sql import SparkSession

def run():
    spark = SparkSession.builder \
        .appName("repartition-testing") \
        .getOrCreate()

    print("* Spark Session is Running...")

    data = [
        (1, "João", 1000),
        (2, "Maria", 2000),
        (3, "Pedro", 3000),
        (4, "Ana", 4000),
        (5, "Carlos", 5000)
    ]

    df = spark.createDataFrame(data, ["id", "nome", "valor"])
    df.printSchema()

    spark.stop()

if __name__ == "__main__":
    run()