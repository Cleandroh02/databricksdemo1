# Databricks notebook source

from pyspark.sql import SparkSession


# Create a Spark session
spark = SparkSession.builder.appName("ETLDemo").getOrCreate()

# COMMAND ----------

# MAGIC
# MAGIC %run "./utils"
# MAGIC

# COMMAND ----------


# Simulate data with null values
num_rows = 10000
simulated_data_with_nulls_df = simulate_data_with_nulls(num_rows)


display(simulated_data_with_nulls_df)


# COMMAND ----------

# Define the file path
parquet_file_path = "/dbfs/tmp/simulated_data_with_nulls.parquet"
# Save data to Parquet file
save_to_parquet(simulated_data_with_nulls_df, parquet_file_path)

# COMMAND ----------


