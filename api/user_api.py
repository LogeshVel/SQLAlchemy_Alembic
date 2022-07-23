from fastapi import APIRouter, HTTPException
from starlette import status

from api.user_model import UserModel
from db.database import sql_engine, Base
from db.db_worker import read_all_users, read_user, add_user, update_db_user, delete_db_user

user_api = APIRouter(prefix="/users", tags=['Users',])
Base.metadata.create_all(bind=sql_engine)


@user_api.get('/')
async def get_all_users():
    return read_all_users()


@user_api.get('/{user_id}')
async def get_user(user_id: int):
    u = read_user(user_id)
    if u is None:
        raise HTTPException(status_code=404, detail="Given user id doesn't exists")
    return u


@user_api.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(user: UserModel):
    return add_user(user)


@user_api.put('/{user_id}')
async def update_user(user_id: int, user: UserModel):
    return update_db_user(user_id, user)


@user_api.delete('/{user_id}')
async def delete_user(user_id: int):
    return delete_db_user(user_id)
