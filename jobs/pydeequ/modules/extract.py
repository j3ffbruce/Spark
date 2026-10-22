from pyspark.sql import DataFrame

class Extract:

    def __init__(self, spark):
        self.spark = spark

    def __extract_datasource_movies(self):
        data: DataFrame = (
            self.spark.read.csv(
                path=".\datasets\csv\movies",
                inferSchema=True,
                header=True,
                sep=";",
                encoding="UTF-16",
            )
        )
        return data

    def run(self):
        data: DataFrame = self.__extract_datasource_movies()
        return data