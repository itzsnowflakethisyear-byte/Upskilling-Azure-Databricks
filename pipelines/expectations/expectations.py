import dlt

# Warn (defaulty)/ Fail / Drop Rows
# @dlt.expect_all_or_fail
# @dlt.expect_all_or_drop
expectations = {
    "rule1" : "sales_id IS NOT NULL",
    "rule2" : "quantity IS NOT NULL",
}

@dlt.table(
    name = "expect_table"
)
@dlt.expect_all(expectations)
def expect_table():
    df = spark.read.table("databrickskrishna.silver.sales_enr")
    return df