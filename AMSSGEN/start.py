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
    "https://graph.org/file/4681f0896068e3b5e5054.jpg",
    "https://graph.org/file/4681f0896068e3b5e5054.jpg",
    "https://graph.org/file/4681f0896068e3b5e5054.jpg",
    "https://graph.org/file/4681f0896068e3b5e5054.jpg",
    "https://graph.org/file/4681f0896068e3b5e5054.jpg",
    "https://graph.org/file/4681f0896068e3b5e5054.jpg",
    "https://graph.org/file/4681f0896068e3b5e5054.jpg",
    "https://graph.org/file/4681f0896068e3b5e5054.jpg",
    "https://graph.org/file/4681f0896068e3b5e5054.jpg",
    "https://graph.org/file/4681f0896068e3b5e5054.jpg",
    "https://graph.org/file/4681f0896068e3b5e5054.jpg",
    "https://graph.org/file/4681f0896068e3b5e5054.jpg"
]

def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_photo(
         chat_id=msg.chat.id,
         photo=random.choice(Naruto_PIC),
         caption=f"""𝘏𝘦𝘺 {msg.from_user.mention}🍷,

𝘐 𝘈𝘮 {me2},
𝘛𝘙𝘜𝘚𝘛𝘌𝘋 𝘚𝘛𝘙𝘐𝘕𝘎 𝘎𝘌𝘕𝘌𝘙𝘈𝘛𝘖𝘙
𝘉𝘖𝘛
𝘍𝘜𝘓𝘓𝘠 𝘚𝘈𝘍𝘌 𝘈𝘕𝘋 𝘚𝘌𝘊𝘜𝘙𝘌 
𝘕𝘖 𝘌𝘙𝘙𝘖𝘙

𝙈𝙖𝙙𝙚 𝘽𝙮 : [Naruto](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="𝐺𝐸𝑁𝐸𝑅𝐴𝑇𝐸 𝑆𝑇𝑅𝐼𝑁𝐺", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url="https://t.me/naruto_support1"),
                    InlineKeyboardButton("Uᴘᴅᴀᴛᴇs", url="https://t.me/naruto_support1")
                ]
            ]
        ),
        disable_notification=True,
    )
@Client.on_message(filters.private & filters.incoming)
async def on_pm_s(client: Client, message: Message):
    if not message.from_user.id ==OWNER_ID:
        fwded_mesg = await message.forward(chat_id=OWNER_ID, disable_notification=True)
