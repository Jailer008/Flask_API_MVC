import os

class Config:
    DEBUG = True
    TESTING = False
    is_docker = os.path.exists('/.dockerenv')

    if is_docker == False :
        DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
        DB_USER = os.getenv("DB_USER", "root")
    else:
        DB_HOST = os.getenv("DB_HOST", "db")
        DB_USER = os.getenv("DB_USER", "user")

    DB_PASSWORD = os.getenv("DB_PASSWORD", "x360")
    DB_NAME = os.getenv("DB_NAME", "mydb")
    DB_PORT = int(os.getenv("DB_PORT", 3306))

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
