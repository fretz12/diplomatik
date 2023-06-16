---
title: Configuration
layout: default
nav_order: 5
---

# Configuration

The Diplomatik service is configured via environment variables passed to the Docker container. 

{: .note }
We currently provide only a singleton database user. Multiple and managed database users will be coming in the future.

--- 

**POSTGRES_DEFAULT_USER**

Data Type: String

Default: `null`

The user for the Postgres database. 
Example: `postgres`

---
**POSTGRES_DEFAULT_PASSWORD**

Data Type: String

Default: `null`

The password for the Postgres user.
Example: `my_secret`

---
**POSTGRES_DEFAULT_HOST**

Data Type: String

Default: `null`

The host for the Postgres database.
Example: `localhost`

---
**POSTGRES_DEFAULT_PORT**

Data Type: Integer

Default: `5432`

The port for the Postgres database.
Example: `5432`

---
**POSTGRES_DEFAULT_DATABASE**

Data Type: String

Default: `null`

The name of the Postgres database
Example: `postgres`

