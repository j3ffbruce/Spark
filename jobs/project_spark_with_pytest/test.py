# test_pyspark_job.py

import pytest
from main import PySparkJob

class TestDataContractTest:  
    @pytest.fixture(scope="class")
    def spark_job(self):
        job = PySparkJob(master_url="local[*]")
        return job

    def test_data_frame_is_not_empty(self, spark_job):
        df = spark_job.process_data()
        assert df.count() > 0, "DataFrame is empty!"

    def test_column_types(self, spark_job):
        df = spark_job.process_data()
        column_types = dict(df.dtypes)
        assert column_types['Name'] == 'string', f"Expected 'string' for 'Name', but got {column_types['Name']}"
        assert column_types['Value'] == 'int', f"Expected 'int' for 'Value', but got {column_types['Value']}"


class TestBusinessRuleTest:
    @pytest.fixture(scope="class")
    def spark_job(self):
        job = PySparkJob(master_url="spark://spark-master:7077")
        return job

    def test_value_column_positive(self, spark_job):
        df = spark_job.process_data()
        assert df.filter(df['Value'] <= 0).count() == 0, "Business rule violated: Some 'Value' entries are less than or equal to zero."