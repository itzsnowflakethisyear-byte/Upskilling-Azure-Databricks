-- Python UDFs for databrickskrishna.bronze

-- Python Scalar Function
CREATE OR REPLACE FUNCTION databrickskrishna.bronze.python_scalar_func(p_par INT)
RETURNS INT
LANGUAGE PYTHON
AS
$$
    import requests
    # Add your Python code here
    return p_par * 2
$$;

-- Add more Python UDFs here

