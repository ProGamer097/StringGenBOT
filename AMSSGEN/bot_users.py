from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram import *
from pyrogram.types import *
from config import OWNER_ID
from AMSSGEN.db.users import add_served_user, get_served_users

@Client.on_message(filters.private & ~filters.service, group=1)
async def users_sql(_, msg: Message):
    await add_served_user(msg.from_user.id)

@Client.on_message(filters.user(OWNER_ID) & filters.command("stats"))
async def _stats(_, msg: Message):
    users = len(await get_served_users())
    await msg.reply_text(f"» ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛs ᴏғ sᴛʀɪɴɢ ɢᴇɴ ʙᴏᴛ :\n\n {users} ᴜsᴇʀs", quote=True)

async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=user_id)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : blocked the bot\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception:
        return 500, f"{user_id} : {traceback.format_exc()}\n"

@Client.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast(_, message):
    if not message.reply_to_message:
        await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ɪᴛ.")
        return
    
    exmsg = await message.reply_text("sᴛᴀʀᴛᴇᴅ ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ!")
    all_users = await get_served_users()  # Use get_served_users directly
    done_users = 0
    failed_users = 0

    for user in all_users:
        try:
            await send_msg(user, message.reply_to_message)
            done_users += 1
            await asyncio.sleep(0.1)
        except Exception:
            pass
            failed_users += 1

    if failed_users == 0:
        await exmsg.edit_text(
            f"**Successfully broadcasting ✅**\n\nSent message to `{done_users}` users",
        )
    else:
        await exmsg.edit_text(
            f"**Successfully broadcasting ✅**\n\nSent message to `{done_users}` users\n\n**Note:** Due to some issues, can't broadcast to `{failed_users}` users.",
        )
