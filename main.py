from uvicorn import run
from fastapi import FastAPI
from src.routes.endpoints import flow_router
from configuration.config import Appconfig
app_config=Appconfig()

app=FastAPI(title=app_config.PROJECT_NAME, openapi_url=app_config.OPENAPI_URL, description=app_config.DESCRIPTION,
        docs_url=app_config.DOCS_URL,
        redoc_url=app_config.REDOC_URL,)

if __name__ == "__main__":
    app.include_router(flow_router)
    run(app, host=app_config.APP_HOST, port=app_config.APP_PORT)