---
title: Get Started
layout: default
nav_order: 2
---

# Get Started

### Prerequisites

- Docker
- Docker Compose
- jq

Please follow installation instructions for above tools

### Step 1. Clone the Repo

```shell
git clone https://github.com/fretz12/diplomatik.git
```
```shell
cd diplomatik
```

### Step 2. Start the Diplomatik Service

Execute the provided Docker Compose script to launch the Diplomatik service and a demo Postgres database locally.
The Postgres database will be the targeted data source where we provide queries to it.

```shell
 docker compose -f deployment/docker/demo/docker-compose.yml up
```

### Step 3. Query the Database

Let's start querying database with Diplomatik's APIs!

First, we'll create a table:

```shell
curl 'http://127.0.0.1:8000/queries/write' \
-H 'Content-Type: application/json' \
-H 'accept: application/json' \
--data-raw '
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
'
'
```

Next, let's add some data:

```shell
curl 'http://127.0.0.1:8000/queries/write' \
-H 'Content-Type: application/json' \
-H 'accept: application/json' \
--data-raw '
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
'
```
With the data in the table, let's see it:

```shell
curl 'http://127.0.0.1:8000/queries/write' \
-H 'Content-Type: application/json' \
-H 'accept: application/json' \
--data-raw '
curl -X POST 'http://127.0.0.1:8000/queries/read' \
-H 'Content-Type: application/json' \
-H 'accept: application/json' \
--data-raw '
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
        "table_name": "my_new_table"
      }
    },
    "fields": [
      {
        "field_type": "column",
        "column_name": "str_column"
      },
      {
        "field_type": "column",
        "column_name": "int_column"
      }
    ]
  }
}
' | jq
```

And we can query it with some basic filtering and math transformations:

```shell
curl -X POST 'http://127.0.0.1:8000/queries/read' \
-H 'Content-Type: application/json' \
-H 'accept: application/json' \
--data-raw '
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
        "table_name": "my_new_table"
      }
    },
    "fields": [
      {
        "field_type": "column",
        "column_name": "str_column"
      },
      {
        "field_type": "value",
        "expression": "__field_placeholder__ * 2 + 10",
        "fields": [
          {
            "field_type": "column",
            "column_name": "int_column"
          }
        ],
        "alias": "my_transformed_column"
      }
    ],
    "filter": {
      "filter_type": "or",
      "filters": [
        {
          "filter_type": "equals",
          "lhs": {
            "field_type": "column",
            "column_name": "str_column"
          },
          "rhs": {
            "field_type": "value",
            "expression": "A"
          }
        },
        {
          "filter_type": "equals",
          "lhs": {
            "field_type": "column",
            "column_name": "int_column"
          },
          "rhs": {
            "field_type": "value",
            "expression": "30"
          }
        }
      ]
    }
  }
}
' | jq
```

That's it! For more examples, head over [here](https://fretz12.github.io/diplomatik/examples/examples.html)