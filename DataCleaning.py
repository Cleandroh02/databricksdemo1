# Databricks notebook source
from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("SimulateSavedRead").getOrCreate()




# COMMAND ----------

# MAGIC
# MAGIC %run "./utils"
# MAGIC

# COMMAND ----------

# Define the file path
parquet_file_path = "/dbfs/tmp/simulated_data_with_nulls.parquet"

# Read data from Parquet file
read_data_with_nulls_df = read_from_parquet(parquet_file_path)

#display(read_data_with_nulls_df.limit(10))


# COMMAND ----------

imputed_data_df = impute_nulls(read_data_with_nulls_df, {'feature3': 2})

# Display the first few rows of the imputed data
#display(imputed_data_df.limit(10))

# COMMAND ----------

save_to_parquet(imputed_data_df, "/dbfs/tmp/cleaned_dataset.parquet")

# COMMAND ----------


