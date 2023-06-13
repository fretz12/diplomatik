---
title: Select Query
nav_order: 2
parent: Search Query
grand_parent: Examples
layout: default
---
# Select Query Examples

## Select From a Single Table
<br>
To get the SQL equivalent of:

```sql
SELECT str_column, decimal_column, date_column AS date
FROM table1
```

Set the payload for `/queries/read` API request as:

```json
{
  "query_type": "search",
  "data_source_config": {
    "source_type": "postgres"
  },
  "query_id": "my_unique_id",
  "source_extraction": {
    "query_type": "select",
    "extraction_type": "select",
    "source_formation": {
      "formation_type": "single_table",
      "table": {
        "table_name": "table1"
      }
    },
    "fields": [
      {
        "field_type": "column",
        "column_name": "str_column"
      },
      {
        "field_type": "column",
        "column_name": "decimal_column"
      },
      {
        "field_type": "column",
        "column_name": "date_column",
        "alias": "date"
      }
    ]
  }
}
```

---

## Select From Joined Tables
<br>
To get the SQL equivalent of:

```sql
SELECT table1.str_column, lookup_table1.lookup_attr1 
FROM table1 
    INNER JOIN lookup_table1 ON table1.str_column = lookup_table1.lookup_id
```

Set the payload for `/queries/read` API request as:

```json
{
  "query_type": "search",
  "data_source_config": {
    "source_type": "postgres"
  },
  "query_id": "my_unique_id",
  "source_extraction": {
    "query_type": "select",
    "extraction_type": "select",
    "source_formation": {
      "formation_type": "join",
      "left_table": {
        "table_name": "table1"
      },
      "right_tables": [
        {
          "join_type": "inner",
          "table": {
            "table_name": "lookup_table1"
          },
          "on_condition": {
            "filter_type": "equals",
            "lhs": {
              "field_type": "column",
              "column_name": "str_column",
              "table_name": "table1"
            },
            "rhs": {
              "field_type": "column",
              "column_name": "lookup_id",
              "table_name": "lookup_table1"
            }
          }
        }
      ]
    },
    "fields": [
      {
        "field_type": "column",
        "column_name": "str_column",
        "table_name": "table1"
      },
      {
        "field_type": "column",
        "column_name": "lookup_attr1",
        "table_name": "lookup_table1"
      }
    ]
  }
}
```

---