from fastapi import FastAPI
from api.user_api import user_api
from api.v2.user_api import user_api as v2_user_api
app = FastAPI()

app.include_router(user_api)
app.include_router(v2_user_api)