-- Table-Valued Functions (UDTFs) for databrickskrishna.bronze

-- UDTF Example
CREATE OR REPLACE FUNCTION databrickskrishna.bronze.udtf(input_value STRING)
RETURNS TABLE(result STRING)
RETURN SELECT input_value AS result;

-- Add more UDTFs here

