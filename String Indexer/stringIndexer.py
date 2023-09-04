# String Indexer - indexes the string
from pyspark.ml.features import StringIndexer

# creates numeric indexed output column for string col
indexer = StringIndexer(inputCol='string', outputCol='output')
index = indexer.fit('df')
index = index.transform('df')

# index is the resultant data frame