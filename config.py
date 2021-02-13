import os

herokupsqluri = "postgres://whbpuqkupdgwjv:4b4e7d6a60c5a7d6f71baa1eb4a845224bc9522558b3623bcae7767f6781b4ef@ec2-34-230-167-186.compute-1.amazonaws.com:5432/d81ihs21ha9mif"

class Config:
    SECRET_KEY = "too hard to decypher string"

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI") or herokupsqluri
    DEBUG = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_DATABASE_URI") or herokupsqluri

config_dict = {
    "DEV": DevelopmentConfig,
    "PROD": ProductionConfig,
    "default": DevelopmentConfig
}