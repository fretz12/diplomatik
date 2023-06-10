---
title: Select Query With Filters
nav_order: 3
parent: Search Query
grand_parent: Examples
layout: default
---
# Select Query Examples

## Select Where Two Columns are (Not) Equal
<br>
To get the SQL equivalent of:

```sql
SELECT str_column, decimal_column
FROM table1
WHERE decimal_column = decimal_column2
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
      }
    ],
    "filter": {
      "filter_type": "equals",
      "lhs": {
        "field_type": "column",
        "column_name": "decimal_column"
      },
      "rhs": {
        "field_type": "column",
        "column_name": "decimal_column2"
      }
    }
  }
}
```

---

## Select Where a Column is (Not) Equal to a Literal Value
<br>
To get the SQL equivalent of:

```sql
SELECT str_column, decimal_column
FROM table1
WHERE decimal_column = 10
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
      }
    ],
    "filter": {
      "filter_type": "equals",
      "lhs": {
        "field_type": "column",
        "column_name": "decimal_column"
      },
      "rhs": {
        "field_type": "value",
        "expression": "10"
      }
    }
  }
}
```

---

## Select Where a Column is (Not) Equal to a Math Formula
<br>
To get the SQL equivalent of:

```sql
SELECT str_column, decimal_column
FROM table1
WHERE decimal_column = decimal_column2 + 10
```

Set the payload for `/queries/read` API request as shown below. Note that for value fields, any referenced field 
names must be set with `__field_placeholder__` which will later be replaced properly with the defined field.

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
      }
    ],
    "filter": {
      "filter_type": "equals",
      "lhs": {
        "field_type": "column",
        "column_name": "decimal_column"
      },
      "rhs": {
        "field_type": "value",
        "expression": "__field_placeholder__ + 10",
        "fields": [
          {
            "field_type": "column",
            "column_name": "decimal_column2"
          }
        ]
      }
    }
  }
}
```

---

## Select Where a Column is Bound Between Two Values
<br>
To get the SQL equivalent of:

```sql
SELECT str_column, decimal_column
FROM table1
WHERE decimal_column >= 5 AND decimal_column < 10
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
      }
    ],
    "filter": {
      "filter_type": "bound",
      "field": {
        "field_type": "column",
        "column_name": "decimal_column"
      },
      "lower": {
        "field_type": "value",
        "expression": "5"
      },
      "upper": {
        "field_type": "value",
        "expression": "10"
      },
      "upper_strict": "true"
    }
  }
}
```

## Select Where a Column is Bound Compared to Another Column
<br>
To get the SQL equivalent of:

```sql
SELECT str_column, decimal_column
FROM table1
WHERE decimal_column >= decimal_column2
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
      }
    ],
    "filter": {
      "filter_type": "bound",
      "field": {
        "field_type": "column",
        "column_name": "decimal_column"
      },
      "lower": {
        "field_type": "column",
        "column_name": "decimal_column2"
      }
    }
  }
}
```

---

## Select Where (Not) Null
<br>
To get the SQL equivalent of:

```sql
SELECT str_column, decimal_column
FROM table1
WHERE str_column IS NULL
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
      }
    ],
    "filter": {
      "filter_type": "null_check",
      "field": {
        "field_type": "column",
        "column_name": "str_column"
      }
    }
  }
}
```

---

## Select Where (Not) Like
<br>
To get the SQL equivalent of:

```sql
SELECT str_column, decimal_column
FROM table1
WHERE str_column LIKE 'A%'
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
      }
    ],
    "filter": {
      "filter_type": "like",
      "field": {
        "field_type": "column",
        "column_name": "str_column"
      },
      "matcher": "A%"
    }
  }
}
```

---

## Select Where (Not) In
<br>
To get the SQL equivalent of:

```sql
SELECT str_column, decimal_column
FROM table1
WHERE str_column IN ('A', 'B', 'C')
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
      }
    ],
    "filter": {
      "filter_type": "matches_any_in",
      "field": {
        "field_type": "column",
        "column_name": "str_column"
      },
      "in_values": [
        "A",
        "B", 
        "C"
      ]
    }
  }
}
```

---