# Databricks notebook source
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("MlModel").getOrCreate()

# COMMAND ----------

# MAGIC %run "./DataCreator"
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %run "./DataCleaning"

# COMMAND ----------

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import BinaryClassificationEvaluator



# COMMAND ----------

# Read the data from "CleanData" notebook
data_path = "/dbfs/tmp/cleaned_dataset.parquet"
cleaned_data_df = spark.read.parquet(data_path)

#display(cleaned_data_df.limit(10))

# COMMAND ----------

# Feature columns
feature_columns = ['feature1', 'feature2', 'feature3']
assembler = VectorAssembler(inputCols=feature_columns, outputCol='features')
assembled_data = assembler.transform(cleaned_data_df)

# Split the data into training and testing sets
train_data, test_data = assembled_data.randomSplit([0.7, 0.3], seed=123)



# COMMAND ----------

# Initialize the Random Forest classifier
rf_classifier = RandomForestClassifier(labelCol='target', featuresCol='features', numTrees=100)

# Create a pipeline for training the model
pipeline = Pipeline(stages=[rf_classifier])

# Train the model
model = pipeline.fit(train_data)




# COMMAND ----------

# Make predictions
predictions = model.transform(test_data)

# Evaluate the model
evaluator = BinaryClassificationEvaluator(labelCol='target', rawPredictionCol='rawPrediction')
auc = evaluator.evaluate(predictions)
print(f"AUC: {auc}")
