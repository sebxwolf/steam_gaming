from start_spark import *
# from utilities import *

################################################################################

## Class to handle spark and df in session
class spark_df_handler:
    """Class to collect spark connection and catch the df in memory.

    Attributes
    ----------
    spark : an initialised spark connection
    df : a spark dataframe that holds the raw data

    Methods
    -------
    load(path, pickle = True)
        Loads a csv

    memorize(df)
        Catch the df in memory
    """

    def __init__(self,
                spark = spark):
        """
        Parameters
        ----------
        """
        self.spark = spark
        self.dfraw = {}

    def load(self, file, delimiter = ',', encoding = "utf-8"):

        self.dfraw[file] = self.spark.read.format("csv").option("header", "true")\
                                    .option("delimiter", ",")\
                                    .option("charset", "utf-8")\
                                    .load(os.path.join(path, file + "*.csv"))


    def memorize(self):
        # Register as table to run SQL queries
        self.df.createOrReplaceTempView("df_table")
        self.spark.sql('CACHE TABLE df_table').collect()

        return self.df
