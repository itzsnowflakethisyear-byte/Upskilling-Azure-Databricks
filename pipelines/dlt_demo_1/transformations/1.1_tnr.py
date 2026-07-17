import dlt
from pyspark.sql.functions import *

# RAW
@dlt.table(
    name = 'sales_stg'
)

def sales_stg():
    df = spark.readStream.option("skipChangeCommits", True)\
    .table("databrickskrishna.silver.sales_enr")
    return df

# Streaming table on append only source
# Mat View on streaming table

# ENRICHED
# CREATE A MAT VIEW
@dlt.table(
    name = 'sales_trn'

)
def sales_trn():
    df = spark.read.table("sales_stg")
    df = df.withColumn("priceAfterDiscount",((col("total_amount") - col("discount"))))

    return df

    # CURATED
@dlt.table(
    name = 'sales_curated'
)
def sales_curated():
    df = spark.read.table("sales_trn")
    return df
