from fastapi import FastAPI

from app.routers import users

app = FastAPI()


@app.get("/")
async def index():
    return {"Hello": "World"}


app.include_router(users.router)
