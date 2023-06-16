# Diplomatik: SQL-Based APIs for Data Analytics and Transformations

Diplomatik is a lightweight and extensible service that adapts a single set of APIs to query a variety of data sources.
Its APIs resemble SQL and act as if you are directly querying the underlying database or data warehouse. 
At the same time, it takes care of datasource compatability and security issues. For example, the same APIs can be used 
to query a Postgres database or a Big Query data warehouse.

Learn more here: https://fretz12.github.io/diplomatik

<p align="center">
  <img src="https://github.com/fretz12/diplomatik/assets/41805201/60e5b0c8-4bbd-4d15-b23f-26cd02acef57" width="400" height="850"/>
</p>


## Why Does it Exist?

SQL is a powerful language used to query and transform data. Applications that allow the end user to explore or manage 
data typically hide it layers deep in the backend. Exposing SQL directly to the end user would put more flexibility 
and power in the user's hands. However, exposing SQL syntax directly via APIs presents some problems:

- Different data sources can have different SQL syntax or DSLs

- The API caller (i.e. a front-end developer) may have no background in writing SQL, let alone figuring out data source 
specific syntax quirks

- Security issues, such as SQL injection attacks

Diplomatik is a middleware service that solves the above problems with a single set of SQL-like APIs and plugs into 
many data sources. It is focused on being developer-oriented, API-first, and extensible for custom scenarios.

## Features

- Single set of APIs to query multiple data sources

- Flexibility and power of SQL expressed in API data models

- Seamless handling of security, multi-tenancy, and permission concerns

- Extensible: build your own SQL-based APIs

- Powerful SQL-based filters, functions, expressions, deep nesting

## Get Started

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

## Supported Data Sources

- Postgres
- More coming soon
