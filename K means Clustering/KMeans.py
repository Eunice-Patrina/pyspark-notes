from pyspark.ml.clustering import KMeans

# we should select k value
kmean = KMeans().setK(2).setSeed(1)
# df should contain column feature or should be specified before
model = kmean.fit(df)
result = model.transform(df)
#result - output dataframe which contains outputCol= prediction

# evaluvate the model
wssse = model.computeCost(df)
print(wssse)

centers = model.clusterCenters()
# centers - list(arr1[n1, n2,.. nk], arr2[], ... arrk[]) where k = 2 in this case