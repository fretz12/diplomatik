---
title: Select Query With Filters
nav_order: 3
parent: Search Query
grand_parent: Examples
layout: default
---
# Select Query Examples

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