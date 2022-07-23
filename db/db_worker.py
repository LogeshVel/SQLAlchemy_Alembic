from fastapi import HTTPException

from db.database import SessionLocal
from db import models
from api.user_model import UserModel


def get_db_instance():
    db = SessionLocal()
    return db


def close_db_instance(db: SessionLocal):
    db.close()


def read_all_users():
    db = get_db_instance()
    r = db.query(models.User).all()
    close_db_instance(db)
    return r


def read_user(id: int):
    db = get_db_instance()
    r = db.query(models.User).filter(models.User.id == id).first()
    close_db_instance(db)
    return r


def add_user(user_details: UserModel):
    db = get_db_instance()
    if is_user_exists(user_details.name, db):
        raise HTTPException(status_code=409, detail="User name already exists")
    user_model = models.User()
    user_model.name = user_details.name
    user_model.age = user_details.age
    user_model.active_user = user_details.active_user
    last_user = get_last_user(db)
    if last_user is None:
        user_model.id = 1
    else:
        last_id = last_user.id
        user_model.id = last_id + 1
    db.add(user_model)
    db.commit()
    close_db_instance(db)
    return {
        "description": "Successfully added the user"
    }


def update_db_user(user_id: int, user_details: UserModel):
    db = get_db_instance()
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Given user id is not found")
    user.name = user_details.name
    user.active_user = user_details.active_user
    user.age = user_details.age
    db.add(user)
    db.commit()
    close_db_instance(db)
    return {
        "description": "Successfully updated the user"
    }


def delete_db_user(user_id: int):
    db = get_db_instance()
    if not is_userid_exists(user_id, db):
        raise HTTPException(status_code=404, detail="Given user id not found")
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()
    close_db_instance(db)
    return {
        "description": "Successfully deleted the user"
    }


def get_last_user(db: SessionLocal):
    all_user = db.query(models.User).all()
    print(all_user)
    if not all_user:
        return None
    return all_user[-1]


def is_user_exists(username: str, db: SessionLocal):
    user = db.query(models.User).filter(models.User.name == username).first()
    if user:
        return True
    return False


def is_userid_exists(userid: int, db: SessionLocal):
    user = db.query(models.User).filter(models.User.id == userid).first()
    if user:
        return True
    return False
