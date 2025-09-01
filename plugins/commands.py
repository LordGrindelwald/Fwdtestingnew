from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config

@Client.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    """Handler for the /start command."""
    await message.reply_text(
        "Hello! I am running correctly.\n\n"
        "Use the /unequify command in a channel to remove duplicate files."
    )
