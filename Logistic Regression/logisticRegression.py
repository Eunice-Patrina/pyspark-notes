from pyspark.ml.classification import LogisticRegression


lr = LogisticRegression()

model = lr.fit(train)

result = model.evaluate(test)
