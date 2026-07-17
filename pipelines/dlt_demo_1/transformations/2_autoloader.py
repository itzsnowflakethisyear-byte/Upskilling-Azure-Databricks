import dlt
from pyspark.sql.functions import * 

# CREATE STREAMING TABLE (AUTOLOADER, aka readStream)
# because we do not have delta table, we neeed to leverage autoloader

# you have raw folder, you want to create streaming tbl, transformaitons and then write the data

@dlt.table(
    name = 'autovol_table'
)
def autovol_table():
    df = spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format", "csv")\
            .load("/Volumes/databrickskrishna/bronze/autovol/raw/")
    return df

# CREATE STREAMING TABLE
@dlt.table(
    name = "autovol_table_enr"
)
def autovol_table_enr():
    df = spark.read.table('autovol_table')
    df = df.withColumn("flag", lit("Yes"))
    return df