import logging
from pyrogram import Client
from config import Config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)

# --- Client Definitions ---

# The user client, which logs in as your user account to scan history
user = Client(
    name="user_session",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    session_string=Config.SESSION
)

# The bot client, which interacts with users
class Bot(Client):
    def __init__(self):
        super().__init__(
            name="bot_session",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(root="plugins")  # Automatically loads all plugins from the 'plugins' folder
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        self.LOGGER.info(f"Bot started as {self.me.first_name}.")
        # Start the user client as well when the bot starts
        await user.start()
        self.LOGGER.info(f"User client started as {user.me.first_name}.")


    async def stop(self, *args):
        await super().stop()
        self.LOGGER.info("Bot stopped.")
        # Stop the user client when the bot stops
        await user.stop()
        self.LOGGER.info("User client stopped.")
