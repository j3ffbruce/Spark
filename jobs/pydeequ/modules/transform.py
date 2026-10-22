from pyspark.sql import DataFrame
from pyspark.sql.functions import col, left, length

class Transform:

    def __init__(self, data):
        self.data = data

    @property
    def __cols_to_rename(self):
        return {"CNPJ_DISTRIBUIDORA�": "CNPJ_DISTRIBUIDORA"}

    def __rename_columns(self, data):
        """Fixing Extra Caracter in Schema"""
        data: DataFrame = (
            data.withColumnsRenamed(
                self.__cols_to_rename
            )
        )
        return data

    @property
    def __clean_cnpj_column(self):
        return left(col("CNPJ_DISTRIBUIDORA"), length(col("CNPJ_DISTRIBUIDORA")) - 1)

    def __add_or_replace_columns(self, data):
        data: DataFrame = (
            data.withColumns(
                {
                    "CNPJ_DISTRIBUIDORA": self.__clean_cnpj_column
                 }
            )
        )
        return data

    def run(self):
        data: DataFrame = self.__rename_columns(data=self.data)
        data: DataFrame = self.__add_or_replace_columns(data=data)
        return data