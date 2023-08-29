# Databricks notebook source
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ETLDemo").getOrCreate()

# COMMAND ----------

import random

def simulate_data_with_nulls(num_rows):
    data = []
    for i in range(1, num_rows + 1):
        feature1 = random.uniform(0, 1)
        feature2 = random.uniform(5, 15)
        feature3 = random.choice([1, None])  # Introduce null values
        target = random.choice([0, 1])
        data.append((i, feature1, feature2, feature3, target))
    columns = ['id', 'feature1', 'feature2', 'feature3', 'target']
    return spark.createDataFrame(data, columns)





def save_to_parquet(dataframe, file_path):
    """Save data to parquet"""
    print("Saving.....")
    dataframe.write.mode("overwrite").parquet(file_path)

# COMMAND ----------

from typing import Dict
# Read data from Parquet file
def read_from_parquet(file_path):
    return spark.read.parquet(file_path)

# Impute null values
def impute_nulls(dataframe, strategy: Dict):
    # Replace null values in 'gender' column with 'Unknown'
    imputed_data = dataframe.fillna(strategy)
    return imputed_data

# COMMAND ----------


