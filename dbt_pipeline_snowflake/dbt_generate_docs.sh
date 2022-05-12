#!/bin/sh
dbt docs generate --profiles-dir ./dbt_profiles
dbt docs serve --profiles-dir ./dbt_profiles