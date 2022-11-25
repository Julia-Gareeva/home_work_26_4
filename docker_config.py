class Config(object):
    """Файл с настройками."""
    SQLALCHEMY_DATABASE_URI = "postgresql://ulia:newrole@postgres/my_database"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 4}
    DEBUG = True
