from pyspark.sql import SparkSession
import pyspark.pandas as ps

class PySparkJob:
    def __init__(self):
        self.spark = SparkSession.builder \
        .config("spark.sql.execution.arrow.pyspark.enabled", "true") \
        .getOrCreate()
        self.spark.sparkContext.setLogLevel("WARN")

    def create_data_frame(self):
        data = {
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Value': [1, 2, 3]
        }

        return ps.DataFrame(data)

if __name__ == "__main__":
    spark_job = PySparkJob()
    df = spark_job.create_data_frame()
    print(df)
