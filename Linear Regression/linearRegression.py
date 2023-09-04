from pyspark.ml.regression import LinearRegression

lr = LinearRegression(featuresCol='features', labelCol='label', predictionCol='prediction')

# train and test are train data frame and test data frame
model = lr.fit(train)

result = model.evaluate(test)

# evaluation metrics
print(result.rootMeanSquaredError)
print(result.r2)