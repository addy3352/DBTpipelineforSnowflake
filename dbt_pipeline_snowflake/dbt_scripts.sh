#!/bin/sh
echo "populating tables from External stage \n"
dbt run-operation load_data_from_external_stage1 --args '{table_name: DBT_DB.SCHEMA_DBT.DBT_DEPARTMENTS}'  --profiles-dir ./dbt_profiles
dbt run-operation load_data_from_external_stage2 --args '{table_name: DBT_DB.SCHEMA_DBT.DBT_AISLES}'  --profiles-dir ./dbt_profiles
dbt run-operation load_data_from_external_stage3 --args '{table_name: DBT_DB.SCHEMA_DBT.DBT_ORDERS}'  --profiles-dir ./dbt_profiles
dbt run-operation load_data_from_external_stage4 --args '{table_name: DBT_DB.SCHEMA_DBT.DBT_PRODUCTS}'  --profiles-dir ./dbt_profiles
dbt run-operation load_data_from_external_stage5 --args '{table_name: DBT_DB.SCHEMA_DBT.DBT_ORDER_PRODUCTS__PRIOR}'  --profiles-dir ./dbt_profiles
##########
dbt test --profiles-dir ./dbt_profiles
dbt run --profiles-dir ./dbt_profiles





