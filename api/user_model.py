from pydantic import BaseModel, Field


class UserModel(BaseModel):
    name: str = Field(min_length=5)
    age: int = Field(gt=0, lt=100)
    active_user: bool
