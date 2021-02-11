import os

class Config:
    SECRET_KEY = "too hard to decypher string"

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI") or ""
    DEBUG = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_DATABASE_URI") or ""

config_dict = {
    "DEV": DevelopmentConfig,
    "PROD": ProductionConfig,
    "default": DevelopmentConfig
}