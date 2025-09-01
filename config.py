import os

class Config(object):
    """
    Class to hold all configuration variables from environment settings.
    """
    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = os.environ.get("API_HASH", None)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    SESSION = os.environ.get("SESSION", None)
    DATABASE_URI = os.environ.get("DATABASE_URI", None)
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "forward-bot")
    OWNER_ID = int(os.environ.get("OWNER_ID", 0))

