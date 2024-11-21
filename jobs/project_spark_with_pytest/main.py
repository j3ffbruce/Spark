from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType


class PySparkJob:
    def __init__(self, master_url="local[*]"):
        self.master_url = master_url
        self.spark = SparkSession.builder.master(self.master_url).getOrCreate()
        self.spark.sparkContext.setLogLevel("WARN")

    def create_data_frame(self, data, schema):
        return self.spark.createDataFrame(data, schema)

    def process_data(self):
        schema = StructType([
            StructField('Name', StringType(), True),
            StructField('Value', IntegerType(), True)
        ])
        data = [('Alice', 1), ('Bob', 2), ('Charlie', 3)]

        return self.create_data_frame(data=data, schema=schema)


def run_tests():
    import pytest
    import os
    test_file = os.path.join(os.path.dirname(__file__), "test.py")
    pytest.main([test_file, "-v", "--disable-warnings"])


if __name__ == "__main__":
    spark_job = PySparkJob(master_url="local[*]")
    df = spark_job.process_data()
    df.show()
    run_tests()
    import sys
    print(f"Python sendo usado: {sys.executable}")
