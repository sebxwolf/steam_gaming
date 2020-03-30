from import_packages import *

################################################################################
## Set up spark

# start spark session
spark = SparkSession.builder.master("local[*]") \
.config("spark.driver.maxResultSize", "8g") \
.config("spark.driver.memory", "10g") \
.config("spark.sql.session.timeZone", "UTC") \
.config("spark.sql.execution.arrow.enabled", "true")\
.getOrCreate()

# Set paths
path = os.path.join(os.environ['HOME'], "work/data/steam_gaming_large")
git = os.path.join(os.environ['HOME'], "work/code")
