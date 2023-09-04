from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('app-name').getOrCreate()

# df - data frame from csv file
df = spark.read.csv('data.csv')

# df - data frame from txt file(JSON)
df = spark.read.format('libsum').load('data.txt')