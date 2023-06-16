---
title: Insert Query
nav_order: 3
parent: Examples
layout: default
---
# Insert Query Examples

## Insert Values Into a Table
<br>
To get the SQL equivalent of:

```sql
INSERT INTO table1 (str_column, int_column) 
VALUES 
    ('A', 10),
    ('B', 20),
    ('C', 30)
```

Set the payload for `/queries/write` API request as shown below. Note the order of the values must match the order of 
the columns.

```json
{
  "query_type": "insert",
  "data_source_config": {
    "source_type": "postgres"
  },
  "query_id": "my_unique_id",
  "insert_type": "values",
  "table": {
    "table_name": "my_new_table"
  },
  "columns": [
    {
      "field_type": "column",
      "column_name": "str_column"
    },
    {
      "field_type": "column",
      "column_name": "int_column"
    }
  ],
  "values": [
    [
      "A",
      10
    ],
    [
      "B",
      20
    ],
    [
      "C",
      30
    ]
  ]
}
```

---