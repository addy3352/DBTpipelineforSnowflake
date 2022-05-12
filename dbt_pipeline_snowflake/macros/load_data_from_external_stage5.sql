{% macro load_data_from_external_stage5(table_name) %}
   {% set query  %}
       COPY INTO {{table_name}}
          FROM @STAGE_DBT/order_products__prior.csv
          FILE_FORMAT = ( SKIP_HEADER =1)
          ON_ERROR = 'CONTINUE'
    {% endset %}
    {% set result =run_query(query) %}
    {% do result.print_table() %}
{% endmacro %}

/*
{ % macro get_table_name(mytableName) % }
  mytableName = 'DBT_DB.SCHEMA_DBT' + mytableName
  load_data_from_external_stage(mytableName)
{% endmacro %} */

