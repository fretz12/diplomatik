---
title: Data Source Management Query
nav_order: 4
parent: Examples
layout: default
---
# Data Source Management Query Examples

## Create a New Table
<br>
To get the SQL equivalent of:

```sql
CREATE TABLE IF NOT EXISTS my_new_table 
(id SERIAL PRIMARY KEY, str_column VARCHAR(255), int_column INT NOT NULL)
```

Set the payload for `/queries/write` API request as:

```json
{
  "query_type": "data_source_management",
  "data_source_config": {
    "source_type": "postgres"
  },
  "query_id": "my_unique_id",
  "command": {
    "command_type": "create_table",
    "table_name": "my_new_table",
    "column_definitions": [
      {
        "column_name": "id",
        "data_type": "auto_increment_int",
        "extra_definitions": "PRIMARY KEY"
      },
      {
        "column_name": "str_column",
        "data_type": "string",
        "byte_count": 255
      },
      {
        "column_name": "int_column",
        "data_type": "int32",
        "extra_definitions": "NOT NULL"
      }
    ]
  }
}
```

---