# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE databrickskrishna.bronze.source(
# MAGIC     product_id INT,
# MAGIC     product_name STRING,
# MAGIC     processDate TIMESTAMP
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC INSERT INTO databrickskrishna.bronze.source
# MAGIC VALUES (1,'honey',CURRENT_TIMESTAMP()),
# MAGIC        (2,'bread',CURRENT_TIMESTAMP()),
# MAGIC        (3,'milk', CURRENT_TIMESTAMP())

# COMMAND ----------

# DBTITLE 1,Cell 3
# MAGIC %sql
# MAGIC SELECT * FROM workspace.bronze.scd1_table

# COMMAND ----------

# DBTITLE 1,Cell 4
# MAGIC %sql
# MAGIC SELECT * FROM workspace.default.scd2_table