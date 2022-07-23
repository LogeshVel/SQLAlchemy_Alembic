# SQLAlchemy_Alembic
This repo contains the code for the API server developed using FastAPI. This API Server handles the CRUD operations of the user stored in the database.

## Server Operations
- create user
- get users/user
- update user
- delete user

### Versions
The API has 2 versions with the backward compatibility.
The API version depends on the Database version with the alembic.

The Database has 2 version.
- In the First Version, the Database has the ```user``` table with the following columns
    - id
    - name
    - age
    - active_user
    
- In the Second Version, the ```user``` table has the following columns
    - id
    - name
    - age
    - active_user
    - phone_no
    
So, based on the Database version we could make the API version available to the Clients.

### To use the server
- Clone the repo
- install the required packages
- export the PYTHONPATH with our projects root directory path
- cd to ```api``` folder
- execute the command ```uvicorn main:app```
- to check the swagger docs ```http://localhost:8000/docs```

we could see the both versions of API exposed. But the API version 2 supports only when the Database is Upgraded.

## Alembic

To install
```
pip install alembic
```

To initialize
```
alembic init alembic
```
This creates ```alembic``` directory in the root dir.
Under the ```alembic``` dir ```versions``` dir.
Generating some files in the directories

```
Creating directory C:..\SQLAlchemy_Alembic\alembic ...  done
Creating directory C:..\SQLAlchemy_Alembic\alembic\versions ...  done
Generating C:..\SQLAlchemy_Alembic\alembic.ini ...  done
Generating C:..\SQLAlchemy_Alembic\alembic\env.py ...  done
Generating C:..\SQLAlchemy_Alembic\alembic\README ...  done
Generating C:..\SQLAlchemy_Alembic\alembic\script.py.mako ...  done
Please edit configuration/connection/logging settings in 'C:..SQLAlchemy_Alembic\\alembic.ini' before proceeding.
```

### Edit the alembic.ini file

- Override the sqlalchemy.url variable with our DB url
- Import our Database model in the env.py file under alembic dir

Now we move forward for versioning the Database

```commandline
alembic revision -m "message"
```

This will generate the Python file that makes to write some code to modify the Database with versioning (upgrade and downgrade)

```commandline
(venv) C:\Users\L\PycharmProjects\SQLAlchemy_Alembic>alembic revision -m "creating phone.no column in the user model"
Generating C:\Users\L\PycharmProjects\SQLAlchemy_Alembic\alembic\versions\d4a24c706226_creating_phone_no_column_in_the_user_.py ...  done
```

Now edit the generated file for the upgrade scenario and the downgrade scenario.
For Upgrade, I will add a phone_no column and for Downgrade i will drop that column

```python
def upgrade() -> None:
    op.add_column('user', sa.Column('phone_no', sa.String(), nullable=True))

def downgrade() -> None:
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('phone_no')
```

## Upgrade to our version
```commandline
alembic upgrade <version_id>
```

```commandline
(venv) C:\Users\L\PycharmProjects\SQLAlchemy_Alembic>alembic upgrade d4a24c706226
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> d4a24c706226, creating phone.no column in the user model
```

## Downgrade to the previous version
```commandline
alembic downgrade -1
```

```commandline
(venv) C:\Users\L\PycharmProjects\SQLAlchemy_Alembic>alembic downgrade -1
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running downgrade d4a24c706226 -> , creating phone.no column in the user model
```

# Note

When the Database is upgraded we can use both the API versions v1 and v2. 
But when the database is downgraded we could only use the API version 1 (v1).

**Since only the Upgraded version of the database has the phone_no column in the user table**
