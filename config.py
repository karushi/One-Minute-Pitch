import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://karush:12345@localhost/omp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'DHBHFBHDBFJDNFKDGFJHV24242'

    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
  'development': DevConfig,
  'production': ProdConfig

}
