import os


MAX_LENGTH = 6
# Шаблон короткого адреса из латинских букв и цифр
SHORT_ID_REGEX = r"^[a-zA-Z0-9]+$"


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    JSON_AS_ASCII = False
