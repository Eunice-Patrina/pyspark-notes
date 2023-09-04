from pyspark.ml.features import OneHotEncoder

# indexed is outputCol of String Indexer or similar type
encoder = OneHotEncoder(inputCol='indexed', outputCol='ohe')

model = encoder.fit(df)
result = model.transform(df)

# result is the resultant data frame