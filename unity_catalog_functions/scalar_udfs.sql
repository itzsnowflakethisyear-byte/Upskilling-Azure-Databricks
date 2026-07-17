-- Scalar UDFs for databrickskrishna.bronze

-- SQL Scalar Function
CREATE OR REPLACE FUNCTION databrickskrishna.bronze.sql_scalar_func(input_param STRING)
RETURNS STRING
RETURN CONCAT('Processed: ', input_param);

-- Add more SQL scalar functions here

