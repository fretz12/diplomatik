# Diplomatik: SQL-Based APIs for Data Analytics and Transformations

### What is It?

Diplomatik is a lightweight and extensible service that adapts a single set of APIs to query a variety of data sources.
Its APIs resemble SQL and act as if you are directly querying the underlying database or data warehouse. 
At the same time, it takes care of datasource compatability and security issues. For example, the same APIs can be used 
to query a Postgres database or a Big Query data warehouse.


### Why Does it Exist?

SQL is a powerful language used to query and transform data. Applications that allow the end user to explore or manage 
data typically hide it layers deep in the backend. Exposing SQL directly to the end user would put more flexibility 
and power in the user's hands. However, exposing SQL syntax directly via APIs presents some problems:

- Different data sources can have different SQL syntax or DSLs

- The API caller (i.e. a front-end developer) may have no background in writing SQL, let alone figuring out data source 
specific syntax quirks

- Security issues, such as SQL injection attacks

Diplomatik is a middleware service that solves the above problems with a single set of SQL-like APIs and plugs into 
many data sources. It is focused on being developer-oriented, API-first, and extensible for custom scenarios.

### Features

- Single set of APIs to query multiple data sources

- Flexibility and power of SQL expressed in API data models

- Seamless handling of security, multi-tenancy, and permission concerns

- Extensible: build your own SQL-based APIs

## Get Started

### Supported Data Sources

- Postgres
- More coming

## Developer Guide

Please visit [here](https://fretz12.github.io/diplomatik/)
