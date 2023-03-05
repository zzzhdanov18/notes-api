from fastapi import FastAPI

from src.routes.router import api_router

app = FastAPI()

app.include_router(api_router)

