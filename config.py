import os

class Config:
    """
    Class to hold all configuration variables loaded from environment variables.
    """
    # Essential Pyrogram variables from my.telegram.org
    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = os.environ.get("API_HASH", "")

    # Your bot's token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # The session string for your user account, obtained by running a session generator script
    SESSION = os.environ.get("SESSION", "")

    # Your MongoDB database URI
    DATABASE_URI = os.environ.get("DATABASE_URI", "")
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "forward-bot")

    # Your Telegram user ID
    OWNER_ID = int(os.environ.get("OWNER_ID", 0))
