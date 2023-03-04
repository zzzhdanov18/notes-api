from fastapi import FastAPI
import uvicorn

app = FastAPI

if __name__ == "main":
    uvicorn.run(app)