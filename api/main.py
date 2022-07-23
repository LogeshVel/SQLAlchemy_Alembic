from fastapi import FastAPI
from api.user_api import user_api
app = FastAPI()

app.include_router(user_api)
