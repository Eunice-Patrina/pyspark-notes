from pyspark.ml.linalg import Vectors
from pyspark.ml.feaature import VectorAssembler

# assembler merges multiple columns into single column
# usually this is final step before modeling phase
# inputCol all feature Column
assembler = VectorAssembler(inputCol=[col1, col2, col3],outputCol='features')

output = assembler.transform(df)
# output is resultant of assembler

