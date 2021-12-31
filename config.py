import os, logging


TORTOISE_ORM = {
    "connections": {
        "default": os.environ.get(
            "DATABASE_URL", "postgres://postgres:postgres@localhost:5432/journal-app"
        )
    },
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        }
    },
}


class BaseConfig:
    DB_URL = os.environ.get(
        "DATABASE_URL", "postgres://postgres:postgres@localhost:5432/journal-app"
    )


class DevelopmentConfig(BaseConfig):
    LOG_LEVEL = logging.DEBUG


class TestingConfig(BaseConfig):
    LOG_LEVEL = logging.INFO


class StagingConfig(BaseConfig):
    LOG_LEVEL = logging.INFO


class ProductionConfig(BaseConfig):
    LOG_LEVEL = logging.INFO


environ = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig,
}

current_env = environ[os.environ.get("ENV", "development")]
