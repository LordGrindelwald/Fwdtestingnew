from pyrogram import Client, filters
from pyrogram.types import Message
import logging
import asyncio

# This imports the 'user' client that was defined in bot.py
from bot import user

LOGGER = logging.getLogger(__name__)

@Client.on_message(filters.command("unequify"))
async def unequify_command(client: Client, message: Message):
    """
    Finds and deletes duplicate media files in a chat.
    Uses 'user' client to scan history and 'bot' client to manage messages.
    """
    seen_files = set()
    messages_to_delete = []

    try:
        await message.reply_text("✅ **Starting Scan...**\n\nI will now check for duplicate files. This may take a moment.")
    except Exception as e:
        LOGGER.error(f"Could not send initial reply in chat {message.chat.id}: {e}")
        return

    try:
        async for msg in user.get_chat_history(message.chat.id):
            file_id = None
            
            if msg.document:
                file_id = msg.document.file_unique_id
            elif msg.video:
                file_id = msg.video.file_unique_id
            elif msg.audio:
                file_id = msg.audio.file_unique_id
            
            if file_id:
                if file_id in seen_files:
                    # **CRITICAL FIX:** Changed 'msg.message_id' to the correct Pyrogram attribute 'msg.id'.
                    messages_to_delete.append(msg.id)
                else:
                    seen_files.add(file_id)

        if messages_to_delete:
            await client.send_message(message.chat.id, f"Found and deleting {len(messages_to_delete)} duplicate files.")
            
            for i in range(0, len(messages_to_delete), 100):
                await client.delete_messages(
                    chat_id=message.chat.id,
                    message_ids=messages_to_delete[i:i + 100]
                )
                await asyncio.sleep(1)
                
            await client.send_message(message.chat.id, "✅ **Cleanup Complete!**")
        else:
            await client.send_message(message.chat.id, "✅ No duplicate files were found.")
            
    except Exception as e:
        LOGGER.error(f"A critical error occurred during the unequify scan in chat {message.chat.id}: {e}")
        await client.send_message(message.chat.id, f"❌ **Error!** An unexpected error occurred: {e}")
