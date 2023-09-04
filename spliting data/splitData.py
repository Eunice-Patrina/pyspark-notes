# create train and test data from single data frame (df)

# train and test data - 70% + 30%
train, test = df.randomSplit([0.7, 0.3])

# train and test data - 80% + 20%
train, test = df.randomSplit([0.8, 0.2])