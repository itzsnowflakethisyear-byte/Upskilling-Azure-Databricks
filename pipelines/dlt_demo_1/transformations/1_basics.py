import dlt
# CREATE A STREAMING TABLE

# We use decorators with function
@dlt.table(
    name = 'demo_stream_table' # if you don't mention name here, it picks function's name (both names should match)
)
def demo_stream_table():
    df = spark.readStream.table('databrickskrishna.silver.sales_enr')
    # By default streaming tables are append only, we do not expect them to change
    # When you know that the table is append only, you can use 'skipChangedColumns', true
    #df = spark.readStream.OPTION('skipChangedColumns', true).table('databrickskrishna.silver.sales_enr')
    return df
# the results of this return is sent to the decorator of the function (name)

# CREATE MATERIALISED VIEW
@dlt.table(
    name = 'demo_mat_view'
)
def demo_mat_view():
    # you're doing read.table, it materalise's the table
    df = spark.read.table('databrickskrishna.silver.sales_enr')
    return df
# the results of this return is sent to the decorator of the function (name)

# TEMPORARY VIEW (BATCH)
@dlt.view(
    name = 'demo_temp_view'
)
def demo_temp_view():
    # you're doing read.table, it materalise's the table
    df = spark.read.table('databrickskrishna.silver.sales_enr')
    return df

# TEMPORARY VIEW (STREAMING)
@dlt.view(
    name = 'demo_temp_view_stream'
)
def demo_temp_view_stream():
    # you're doing read.table, it materalise's the table
    df = spark.readStream.table('databrickskrishna.silver.sales_enr')
    return df


