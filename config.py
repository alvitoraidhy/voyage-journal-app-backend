import os, logging


class BaseConfig:
    DB_URL = os.environ["DATABASE_URL"]


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
