from pydeequ.analyzers import *
from pydeequ.profiles import *
from pydeequ.verification import *
from pydeequ.checks import *

class Quality:

    def __init__(self, spark, data):
        self.spark = spark
        profile_cols = ["TITULO_BRASIL", "PUBLICO"]

        self.analyzer_runner = (
            AnalysisRunner(self.spark)
            .onData(data)
        )

        self.profile_runner = (
            ColumnProfilerRunner(self.spark)
            .onData(
                data.select(*profile_cols)
            )
        )

        self.check_obj = Check(
            self.spark, CheckLevel.Warning,
            "PyDeequ Check - Check"
        )

        self.check_runner = (
            VerificationSuite(self.spark)
            .onData(data)
        )

    def __build_dataset_analyzers(self):
        self.analyzer_runner = (
            self.analyzer_runner
            .addAnalyzer(Size())
        )

    def __build_columns_analyzers(self):
        self.analyzer_runner = (
            self.analyzer_runner
            .addAnalyzer(Completeness("CNPJ_DISTRIBUIDORA"))
            .addAnalyzer(CountDistinct("CNPJ_DISTRIBUIDORA"))
            .addAnalyzer(Compliance("PUBLICO", "PUBLICO > 10"))
        )

    def __execute_analyzer(self):
        self.__build_dataset_analyzers()
        self.__build_columns_analyzers()
        response = self.analyzer_runner.run()
        return response

    def __output_analyzer(self, analyzer_response):
        data = (
            AnalyzerContext.successMetricsAsDataFrame(
                self.spark,
                analyzer_response
            )
        )

        data.show(truncate=False)

    def __execute_profile(self):
        profile = (
           self.profile_runner.run()
        )
        return profile

    @staticmethod
    def __output_profile(profile_response):
        for col, profile in profile_response.profiles.items():
            print(col)
            print(profile)

    def __build_check(self):
        self.check_runner = (
            self.check_runner
            .addCheck(
                self.check_obj
                .isUnique("PUBLICO", hint="❌ Failed: Found duplicate values")
                .isNonNegative("PUBLICO", hint="❌ Failed: Found negative values")
            )
        )

    def __execute_check(self):
        self.__build_check()
        response = self.check_runner.run()
        return response

    def __output_check(self, check_response):
        data = VerificationResult.checkResultsAsDataFrame(self.spark, check_response)
        data.show(truncate=False, vertical=True)

    def run(self):
        analyzer_response = self.__execute_analyzer()
        profile_response = self.__execute_profile()
        check_response = self.__execute_check()

        # Show Information
        # self.__output_analyzer(analyzer_response=analyzer_response)
        self.__output_profile(profile_response=profile_response)
        # self.__output_check(check_response=check_response)

