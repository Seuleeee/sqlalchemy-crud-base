# sqlalchemy-crud-base
Please import it into your project. By defining only the database connection information and Model, it provides CRUD operations using SQLAlchemy.

## Tech Stack

- ![Python](https://img.shields.io/badge/python-3.8+-blue.svg) Python 3.8 or higher
- ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.23-green.svg) SQLAlchemy 2.0.23
- ![PostgreSQL](https://img.shields.io/badge/RDBMS-PostgreSQL-blue.svg) RDBMS: PostgreSQL

## Environment Setup

Before running the project, create a `.env` file and set the following environment variables:
These settings are used to connect to the PostgreSQL/MySQL/MariaDB database.

### Usage Instructions

Before using, make sure to install the 'python-dotenv' package. You can set the environment variables as follows:

```python
from dotenv import load_dotenv

# Load environment variables from the specified file
load_dotenv(dotenv_path='.env')
```

#### .env file
```
# DB_TYPE=postgresql+psycopg2
# DB_TYPE=mysql+pymysql
DB_TYPE=postgresql
DB_NAME={database name}
DB_USER={user name}
DB_PASSWORD={password}
DB_HOST={host ip adress}
DB_PORT={host port number}
```
