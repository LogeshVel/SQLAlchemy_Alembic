# SQLAlchemy_Alembic
The FastAPI with the SQLAlchemy that uses the Alembic for the modification and migration of the database


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

## Edit the alembic.ini file

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

