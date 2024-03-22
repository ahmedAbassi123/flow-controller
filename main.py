from uvicorn import run
from fastapi import FastAPI
from src.routes.endpoints import router

app=FastAPI()

if __name__ == "__main__":
    app.include_router(router)
    run(app, host="0.0.0.0", port=8000)