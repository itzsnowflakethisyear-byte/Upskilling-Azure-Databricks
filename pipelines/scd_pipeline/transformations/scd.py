# slowly changing dimension - shared staging table
import dlt
from pyspark.sql.functions import  *

# STAGING TABLE (shared by both SCD Type 1 and Type 2)
@dlt.table(
    name = "scd_stg"
)
def scd_stg():
    df = spark.readStream.table("databrickskrishna.bronze.source")
    return df

# SCD TYPE 1 - CREATE AN EMPTY STREAMING TABLE IN BRONZE SCHEMA
dlt.create_streaming_table(
    name = "workspace.bronze.scd1_table"
)

dlt.create_auto_cdc_flow(
    # Bringing the incremental data
    source = "scd_stg",
    target = "workspace.bronze.scd1_table",
    keys = ["product_id"],
    # To have updated and latest data
    sequence_by = col("processDate"),
    stored_as_scd_type = 1
)

# SCD TYPE 2 - CREATE AN EMPTY STREAMING TABLE
dlt.create_streaming_table(
    name = "scd2_table"
)

dlt.create_auto_cdc_flow(
    # Bringing the incremental data
    source = "scd_stg",
    target = "scd2_table",
    keys = ["product_id"],
    # To have updated and latest data
    sequence_by = col("processDate"),
    stored_as_scd_type = 2
    # Does not allow duplicates, you dont have to write a separate logic each time to enter same data with new data
    #expect_column_list ['processDate']
)