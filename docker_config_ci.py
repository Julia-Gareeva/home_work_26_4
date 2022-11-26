class Config(object):
    """Файл с настройками."""
    SQLALCHEMY_DATABASE_URI = "postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@postgres/$POSTGRES_DB"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 4}
    DEBUG = True
