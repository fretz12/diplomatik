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