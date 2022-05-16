import os

isDev = os.getenv("ENV") == "dev"


class AppConfig:
    # db_tracking_charset = os.getenv("DB_TRACKING_CHARSET")
    APP_NAME = "ContactManager"

    isDev = isDev
