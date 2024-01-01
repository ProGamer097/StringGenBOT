from config import MONGO_DB_URI
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

mongo = MongoCli(MONGO_DB_URI)
db = mongo.users
db = mongo.chats
db = db.chatsdb
db = db.users

#users
async def get_users():
  user_list = []
  async for user in db.users.find({"user": {"$gt": 0}}):
    user_list.append(user['user'])
  return user_list


async def get_user(user):
  users = await get_users()
  if user in users:
    return True
  else:
    return False

async def add_user(user):
  users = await get_users()
  if user in users:
    return
  else:
    await db.users.insert_one({"user": user})


async def del_user(user):
  users = await get_users()
  if not user in users:
    return
  else:
    await db.users.delete_one({"user": user})

#chats

async def get_chats():
  chat_list = []
  async for chat in db.chats.find({"chat": {"$lt": 0}}):
    chat_list.append(chat['chat'])
  return chat_list

async def get_chat(chat):
  chats = await get_chats()
  if chat in chats:
    return True
  else:
    return False

async def add_chat(chat):
  chats = await get_chats()
  if chat in chats:
    return
  else:
    await db.chats.insert_one({"chat": chat})

async def del_chat(chat):
  chats = await get_chats()
  if not chat in chats:
    return
  else:
    await db.chats.delete_one({"chat": chat})
