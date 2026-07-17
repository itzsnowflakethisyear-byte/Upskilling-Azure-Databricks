# Upskilling Azure Databricks

This repository contains all my Databricks learning projects including ETL pipelines, Unity Catalog functions, and notebooks.

## Repository Structure

```
├── pipelines/                    # Spark Declarative Pipelines (SDP/DLT)
│   └── scd_pipeline/            # Slowly Changing Dimension pipeline
│       └── transformations/     # Pipeline transformation files
│           ├── scd.py          # SCD Type 1 & 2 implementation
│           └── my_transformation.py
│
├── unity_catalog_functions/      # Unity Catalog UDFs and UDTFs
│   ├── scalar_udfs.sql          # SQL scalar functions
│   ├── python_udfs.sql          # Python UDFs
│   ├── table_udfs.sql           # Table-valued functions (UDTFs)
│   └── README.md
│
└── notebooks/                    # Analysis and utility notebooks
```

## Getting Started

### Prerequisites
- Azure Databricks workspace
- Unity Catalog enabled
- Access to databrickskrishna catalog

### Deploying Pipelines
1. Navigate to the Databricks UI
2. Create a new pipeline
3. Set the source to this repository's `pipelines/` directory
4. Configure target catalog and schema
5. Run the pipeline

### Deploying UC Functions
Run each SQL file in the `unity_catalog_functions/` directory in Databricks SQL Editor or notebook.

## Learning Resources
- [Azure Databricks Documentation](https://docs.databricks.com/en/index.html)
- [Unity Catalog Guide](https://docs.databricks.com/en/data-governance/unity-catalog/index.html)
- [Spark Declarative Pipelines](https://docs.databricks.com/en/delta-live-tables/index.html)

