# sqlalchemy-crud-base
Please import it into your project. By defining only the database connection information and Model, it provides CRUD operations using SQLAlchemy.

## Tech Stack

- ![Python](https://img.shields.io/badge/python-3.8+-blue.svg) Python 3.8 or higher
- ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.23-green.svg) SQLAlchemy 2.0.23
- ![PostgreSQL](https://img.shields.io/badge/RDBMS-PostgreSQL-blue.svg) RDBMS: PostgreSQL

## Environment Setup

Before running the project, create a `.env` file and set the following environment variables:
These settings are used to connect to the PostgreSQL database.
> :warning: **Currently, only PostgreSQL is supported. Implementation for additional databases like MySQL, MariaDB, etc., is planned for the future. (However, the exact timeline is uncertain...)**
```
DATABASE_PORT=5432
POSTGRES_PASSWORD=password
POSTGRES_USER=postgres
POSTGRES_DB=postgres
POSTGRES_HOST=127.0.0.1
```
