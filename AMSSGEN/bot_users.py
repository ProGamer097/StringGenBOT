from pyrogram.types import Message
from pyrogram import Client, filters

from config import OWNER_ID
from AMSSGEN.db.users import add_served_user, get_served_users


@Client.on_message(filters.private & ~filters.service, group=1)
async def users_sql(_, msg: Message):
    await add_served_user(msg.from_user.id)


@Client.on_message(filters.user(OWNER_ID) & filters.command("stats"))
async def _stats(_, msg: Message):
    users = len(await get_served_users())
    await msg.reply_text(f"» ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛs ᴏғ sᴛʀɪɴɢ ɢᴇɴ ʙᴏᴛ :\n\n {users} ᴜsᴇʀs", quote=True)
    
@Client.on_message(filters.user(OWNER_ID) & filters.command("gcast"))
async def gcast_command(_, msg: Message):
    command_args = msg.command[1:]
    if not command_args:
        await msg.reply_text("Please provide a message to broadcast after /gcast command.")
        return
    served_users = await get_served_users()
    for user_id in served_users:
        try:
            await Client.send_message(user_id, f"Broadcast from the owner:\n\n{' '.join(command_args)}")
        except Exception as e:
            print(f"Failed to send broadcast to user {user_id}: {str(e)}")

    await msg.reply_text(f"Broadcast sent to {len(served_users)} users.")
