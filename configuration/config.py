from pydantic_settings import BaseSettings
from pydantic import Field



class Appconfig(BaseSettings):
    APP_HOST: str = Field( default="0.0.0.0")
    APP_PORT: int = Field( default=8000)
    PROJECT_NAME: str = Field(default="Flow-controller")
    OPENAPI_URL: str = Field(default="/docs/swagger.json")
    DESCRIPTION: str = Field(default="Swagger for Flow-controller")
    DOCS_URL: str = Field(default="/docs")
    REDOC_URL: str = Field(default="/redocs")