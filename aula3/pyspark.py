pip install pyathena
pip install pandas

from pyathena import connect
import pandas as pd

conn = connect(s3_staging_dir='s3://boletos789788789794/' ,
               region_name='us-east-1')
pandasDF= pd.read_sql("SELECT * FROM bancoo.costumers limit 10", conn)
print(pandasDF.head()) 

#parte 28
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Spark DataFrames").getOrCreate()
print(type(pandasDF))

#Create PySpark DataFrame from Pandas
sparkDF=spark.createDataFrame(pandasDF) 
sparkDF.printSchema()
sparkDF.show()


from pyspark.sql.functions import col
print('sparkDF.select(col("customerid"), col("customername")).show()' )
sparkDF.select(col("customerid"), col("customername")).show()

print("sparkDF.select('*').show()")
sparkDF.select('*').show()
print("sparkDF.select(sparkDF.columns[2:6]).show()")
sparkDF.select(sparkDF.columns[2:6]).show()

sparkDF.filter(sparkDF.country == "USA").show()

countryS = ["USA", "France"]
sparkDF.filter(sparkDF.country.isin(countryS)).show()


# # COMMAND ----------

# df.filter(df.course.startswith("USA")).show()

# # COMMAND ----------

# df.filter(df.name.endswith("se")).show()

# # COMMAND ----------

# df.filter(df.name.contains("se")).show()

