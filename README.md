# sqlalchemy-crud-base
Please import it into your project. By defining only the database connection information and Model, it provides CRUD operations using SQLAlchemy.

## Tech Stack

- ![Python](https://img.shields.io/badge/python-3.8+-blue.svg) Python 3.8 or higher
- ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.23-green.svg) SQLAlchemy 2.0.23
- ![PostgreSQL](https://img.shields.io/badge/RDBMS-PostgreSQL-blue.svg) RDBMS: PostgreSQL

## Usage Instructions

### 1. Environment Setup

Before running the project, create a `.env` file in your project  
and set the following environment variables:  
These settings are used to connect to the PostgreSQL/MySQL/MariaDB database.

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


Before using, make sure to install the 'python-dotenv' package.  
You can set the environment variables as follows:

```python
from dotenv import load_dotenv

# Load environment variables from the specified file
load_dotenv(dotenv_path='.env')
```

### 2. Write SqlAlchemy Model schema
The crudalchemy package accepts SQLAlchemy model objects as arguments.  
You are free to change the filename and path as you wish.
#### models.py

```python
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Sequence,
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func


Base = declarative_base()


class ExampleModel(Base):
    __tablename__ = 'example'

    id = Column(Integer, Sequence('example_id_seq'), primary_key=True, index=True)
    example_col = Column(String, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), index=True)
```

### 3. Using crudalchemy for CRUD

By following a few simple steps, you can use the SQLAlchemy model you've defined to perform basic CRUD operations:  

0. Install crudalchemy packages
    ```shell
    pip install git+https://github.com/Seuleeee/sqlalchemy-crud-base
    ```
1. Get a DB session
    > :warning: ** Ensure that you have loaded the .env file using `load_env` before proceeding with the following steps.**
2. Create a CRUD object
3. Apply CRUD operations

#### example.py
#### 1. Create a CRUD object

```python
from crudalchemy.config.connect import get_db
from crudalchemy.crud import CRUDBase

from .models import ExampleModel

# 1. Get a DB session
db = get_db()

# 2. Create a CRUD object
example_crud = CRUDBase(ExampleModel)
```

#### 2. Create

```python
# Dummy Data
create_schema = {
   "question": "What's your favorite?",
   "answer": "BasketBall",
}
create_record = ExampleModel(**create_schema)
created_model = example_crud.create(db, create_record)
```

#### 3. Read
* Single Object
   ```python
   single_model = example_crud.get(db, created_model.id)
   ```
* Multiple Objectg
   ```python
   multiple_model = example_crud.get_multi(db)
   ```

#### 4. Update

```python
# Dummy Data
update_schema = {
   "question": "What's your favorite programming language?",
   "answer": "Python!!!"
}
update_record = ExampleModel(**update_schema)
updated_model = example_crud.update(db, created_model, update_record)
```

#### 5. Delete
```pytghon
delete_record_id = updated_model.id
deleted_record = example_crud.remove(db, delete_record_id)
```


#### 6. Connection Close

```python
db.close()
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or suggestions, please feel free to contact me at [bryantjo1224@gmail.com](mailto:bryantjo1224@gmail.com).


