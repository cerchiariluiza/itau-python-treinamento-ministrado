

#Create PySpark 
from pyspark.sql import SparkSession
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Spark DataFrames").getOrCreate()

simpleData = [("James","Sales","NY",90000,34,10000),
    ("Michael","Sales","NY",86000,56,20000),
    ("Robert","Sales","CA",81000,30,23000),
    ("Maria","Finance","CA",90000,24,23000),
    ("Raman","Finance","CA",99000,40,24000),
    ("Scott","Finance","NY",83000,36,19000),
    ("Jen","Finance","NY",79000,53,15000),
    ("Jeff","Marketing","CA",80000,25,18000),
    ("Kumar","Marketing","NY",91000,50,21000)
  ]

schema = ["employee_name","department","state","salary","age","bonus"]
df = spark.createDataFrame(data=simpleData, schema = schema)
df.printSchema()
df.show(truncate=False)

import datetime
dt = datetime.datetime.now()
print(dt)


from pyspark.sql.functions import lit
from pyspark.sql.functions import when
df.withColumn("age", \
   when((df.age < 30), lit(None)) \
     .when((df.age >= 18) & (df.age <= 60), lit("adulto")) \
     .otherwise(lit("idoso")) \
  ).show()

# Add New column with NULL
df.withColumn("DEFAULT_COL", lit(None)) \
  .show()

# Add New column with NULL
df.withColumn("DEFAULT_COL", lit(dt)) \
  .show()

from pyspark.sql.functions import sum,avg,max,min,mean,count
#//GroupBy on multiple columns
df.groupBy("department","state") \
    .sum("salary","bonus") \
    .show()

#subtptal

#df.groupBy("department").sum("salary").show(truncate=False)
