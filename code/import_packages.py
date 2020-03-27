##### Import packages #####

### spark etc
import os, pyspark, time, sys
import pyspark.sql.functions as F
from pyspark.sql.functions import pandas_udf, PandasUDFType
from pyspark import *
from pyspark.sql import *
from pyspark.rdd import *
from pyspark.ml import *
from pyspark.sql.types import ArrayType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import DoubleType
from pyspark.sql.types import FloatType
import multiprocessing

### data wrangling
import pandas as pd
pd.options.display.float_format = '{:,.0f}'.format
pd.set_option("display.max_rows", 100)
pd.options.display.max_columns = 100
import datetime as dt
import numpy as np
from random import sample, seed
seed(510)
import re
import copy
import json

### plotting
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

### jupyter
from IPython.display import HTML
import warnings
warnings.filterwarnings('ignore')
import os
from IPython.display import display, HTML

display(HTML(data="""
<style>
    div#notebook-container    { width: 95%; }
    div#menubar-container     { width: 65%; }
    div#maintoolbar-container { width: 99%; }
</style>
"""))
