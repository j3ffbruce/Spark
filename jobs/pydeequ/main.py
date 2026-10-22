from pyspark import __version__ as pyspark_version
from pyspark.sql import SparkSession

from pydeequ import __version__ as pydeequ_version
from pydeequ import deequ_maven_coord
from pydeequ import f2j_maven_coord

from modules import Extract, Transform, Quality

class PyDeequJob:

    def __init__(self):
        self.spark = self.__create_spark_session()

    @classmethod
    def __create_spark_session(cls):
        spark = (
            SparkSession.builder
            .config("spark.jars", "/jobs/pydeequ/packages/dqdl-1.0.0.jar")
            .config("spark.jars.packages", deequ_maven_coord)
            .config("spark.jars.excludes", f2j_maven_coord)
            .master("local[*]")
            .appName("pyDeequ")
            .getOrCreate()
        )

        spark.sparkContext.setLogLevel("WARN")

        return spark

    def run_pipeline(self):
        try:
            data = Extract(spark=self.spark).run()
            data = Transform(data=data).run()
            Quality(spark=self.spark, data=data).run()
        finally:
            self.spark.stop()

if __name__ == "__main__":
    print(f"- pyspark version: {pyspark_version}")
    print(f"- pydeequ version: {pydeequ_version}")
    PyDeequJob().run_pipeline()
