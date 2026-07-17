# Unity Catalog Functions

This directory contains all Unity Catalog function definitions for the databrickskrishna catalog.

## Files

- `scalar_udfs.sql` - SQL scalar functions
- `python_udfs.sql` - Python scalar functions  
- `table_udfs.sql` - Table-valued functions (UDTFs)

## Usage

To deploy these functions, run each SQL file in order:

```sql
-- In Databricks SQL or Notebook
%run ./scalar_udfs.sql
%run ./python_udfs.sql
%run ./table_udfs.sql
```

