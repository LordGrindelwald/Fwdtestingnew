import motor.motor_asyncio
from config import Config

# Establish a connection to the MongoDB database
client = motor.motor_asyncio.AsyncIOMotorClient(Config.DATABASE_URI)
db = client[Config.DATABASE_NAME]

# Example database functions (you can add your own logic here)
async def get_user(user_id):
    return await db.users.find_one({'_id': user_id})

async def add_user(user_id):
    if not await get_user(user_id):
        await db.users.insert_one({'_id': user_id})
