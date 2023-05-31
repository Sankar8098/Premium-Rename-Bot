from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**ғʀᴇᴇ ᴘʟᴀɴ ᴜsᴇʀ**
➠ ᴅᴀɪʟʏ  ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 𝟸ɢʙ
➠ ᴘʀɪᴄᴇ : ғʀᴇᴇ
━━━━━━━━━━━━━━━━━━━━━━━
** ᴠɪᴘ 𝟷 ᴘʟᴀɴ ᴜsᴇʀ**
➠ ᴅᴀɪʟʏ  ᴜᴘʟᴏᴀᴅ  ʟɪᴍɪᴛ 𝟷𝟶ɢʙ
➠ ᴘʀɪᴄᴇ ʀs 𝟻𝟻  🇮🇳/🌎 𝟶.𝟼𝟽$  ᴘᴇʀ ᴍᴏɴᴛʜ 
━━━━━━━━━━━━━━━━━━━━━━━
** ᴠɪᴘ 𝟸 ᴘʟᴀɴ ᴜsᴇʀ**
➠ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 𝟻𝟶ɢʙ
➠ ᴘʀɪᴄᴇ ʀs 𝟾𝟶  🇮🇳/🌎 𝟶.𝟿𝟽$  ᴘᴇʀ ᴍᴏɴᴛʜ 
✧━━━━━▣✧❅✦❅✧▣━━━━━✧
         ᴘᴀʏ ᴜsɪɴɢ ᴜᴘɪ ɪ'ᴅ
     ```kunalgaikwad93@axl```
✧━━━━━▣✧❅✦❅✧▣━━━━━✧
 ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛs ᴏғ 
        ᴘᴀʏᴍᴇɴᴛ ᴛᴏ ᴀᴅᴍɪɴ"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ᴀᴅᴍɪɴ 🛂",url = "https://t.me/SexyNano")], 
        			[InlineKeyboardButton("ᴘᴀʏᴘᴀʟ 🌎",url = "https://t.me/SexyNano"),
        			InlineKeyboardButton("ᴜᴘɪ 🥷",url = "https://t.me/SexyNano")],[InlineKeyboardButton("🚫",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**ғʀᴇᴇ ᴘʟᴀɴ ᴜsᴇʀ**
➠ ᴅᴀɪʟʏ  ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 𝟸ɢʙ
➠ ᴘʀɪᴄᴇ : ғʀᴇᴇ
━━━━━━━━━━━━━━━━━━━━━━━
** ᴠɪᴘ 𝟷 ᴘʟᴀɴ ᴜsᴇʀ**
➠ ᴅᴀɪʟʏ  ᴜᴘʟᴏᴀᴅ  ʟɪᴍɪᴛ 𝟷𝟶ɢʙ
➠ ᴘʀɪᴄᴇ ʀs 𝟻𝟻  🇮🇳/🌎 𝟶.𝟼𝟽$  ᴘᴇʀ ᴍᴏɴᴛʜ 
━━━━━━━━━━━━━━━━━━━━━━━
** ᴠɪᴘ 𝟸 ᴘʟᴀɴ ᴜsᴇʀ**
➠ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 𝟻𝟶ɢʙ
➠ ᴘʀɪᴄᴇ ʀs 𝟾𝟶  🇮🇳/🌎 𝟶.𝟿𝟽$  ᴘᴇʀ ᴍᴏɴᴛʜ 
✧━━━━━▣✧❅✦❅✧▣━━━━━✧
         ᴘᴀʏ ᴜsɪɴɢ ᴜᴘɪ ɪ'ᴅ
     ```kunalgaikwad93@axl```
✧━━━━━▣✧❅✦❅✧▣━━━━━✧
 ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛs ᴏғ 
        ᴘᴀʏᴍᴇɴᴛ ᴛᴏ ᴀᴅᴍɪɴ"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ᴀᴅᴍɪɴ 🛂",url = "https://t.me/SexyNano")], 
        			[InlineKeyboardButton("ᴘᴀʏᴘᴀʟ🌎",url = "https://t.me/SexyNano"),
        			InlineKeyboardButton("ᴜᴘɪ 🥷",url = "https://t.me/SexyNano")],[InlineKeyboardButton("🚫",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
