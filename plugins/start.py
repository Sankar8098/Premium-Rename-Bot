import os
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.progress import humanbytes

from helper.database import  insert ,find_one,used_limit,usertype,uploadlimit,addpredata,total_rename,total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import add_date ,check_expi
CHANNEL = os.environ.get('CHANNEL',"Index_AC")
import datetime
from datetime import date as date_
STRING = os.environ.get("STRING","BQBtCcmtxiQNzwe_bnndwMyOQZJ7OXRewlIHruEIR4vwXV11inUHnwO9e7_SC0ipDPt8Wr4Yu0CDBUq5V2DgR_NP0pjBLrAKEYrMbs0x9CVhZdNoKVdXPxUS7cRGBv6cOHc7s06utr38eU9_dhRZr199LDaS9XprpL0dsDcjbCKp8_-uEve4kqKeiaKY3KQngS9VaTUqjswwcsIYzn5lHPBPtK54MMpTkbNGD1R7EMxj35c3Y6G71vwqVd6R7f8ffPhxivM5KDB-CrBvlrRYNERCcp9BHvZ3NYeDBI-T4JIOJRdIHhfR4FyhO2SR0jq83-TBgm5kw6Qz07eyMxHFzD_0AAAAAXd1EakA")
log_channel = int(os.environ.get("LOG_CHANNEL","-1001596651023"))
token = os.environ.get('TOKEN','6295603578:AAEdxq3Nh5zPKMnr-1RfgosDl5Q10Nwj54M')
botid = token.split(':')[0]

#Part of Day --------------------
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
	wish = "ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ."
elif 12 <= currentTime.hour < 12:
	wish = 'ɢᴏᴏᴅ ᴀғᴛᴇʀɴᴏᴏɴ.'
else:
	wish = 'ɢᴏᴏᴅ ᴇᴠᴇɴɪɴɢ.'

#-------------------------------

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	old = insert(int(message.chat.id))
	try:
	    id = message.text.split(' ')[1]
	except:
	    await message.reply_text(text =f"""
	{wish} {message.from_user.first_name }
	ɪ'ᴍ ғɪʟᴇ ʀᴇɴᴀᴍᴇ ʙᴏᴛ, ᴘʟᴇᴀsᴇ sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴅᴏᴄᴜᴍᴇɴᴛs && ᴠɪᴅᴇᴏ ᴀɴᴅ ᴇɴᴛᴇʀ ɴᴇᴡ ғɪʟᴇ ɴᴀᴍᴇ ᴛᴏ ʀᴇɴᴀᴍᴇ ɪᴛ
	""",reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup(
	 [[ InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ 🇮🇳" ,url="https://t.me/Index_AC") ], 
	[InlineKeyboardButton("ᴏᴡɴᴇʀ 🥷", url="https://t.me/SexyNano") ]  ]))
	    return
	if id:
	    if old == True:
	        try:
	            await client.send_message(id,"Your Friend already Using Our Bot")
	            await message.reply_text(text =f"""
	{wish} {message.from_user.first_name }
	ɪ'ᴍ ғɪʟᴇ ʀᴇɴᴀᴍᴇ ʙᴏᴛ, ᴘʟᴇᴀsᴇ sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴅᴏᴄᴜᴍᴇɴᴛs && ᴠɪᴅᴇᴏ ᴀɴᴅ ᴇɴᴛᴇʀ ɴᴇᴡ ғɪʟᴇ ɴᴀᴍᴇ ᴛᴏ ʀᴇɴᴀᴍᴇ ɪᴛ
	""",reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup(
	 [[ InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ 🇮🇳" ,url="https://t.me/Index_AC") ], 
	[InlineKeyboardButton("ᴏᴡɴᴇʀ 🥷", url="https://t.me/SexyNano") ]  ]))
	        except:
	             return
	    else:
	         await client.send_message(id,"Congrats! You Won 100MB Upload limit")
	         _user_= find_one(int(id))
	         limit = _user_["uploadlimit"]
	         new_limit = limit + 104857600
	         uploadlimit(int(id),new_limit)
	         await message.reply_text(text =f"""
	 {wish} {message.from_user.first_name }
**ɪ'ᴍ ғɪʟᴇ ʀᴇɴᴀᴍᴇ ʙᴏᴛ, ᴘʟᴇᴀsᴇ sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴅᴏᴄᴜᴍᴇɴᴛs && ᴠɪᴅᴇᴏ ᴀɴᴅ ᴇɴᴛᴇʀ ɴᴇᴡ ғɪʟᴇ ɴᴀᴍᴇ ᴛᴏ ʀᴇɴᴀᴍᴇ ɪᴛ**
	""",reply_to_message_id = message.id , #ɪ'ᴍ ғɪʟᴇ ʀᴇɴᴀᴍᴇ ʙᴏᴛ, ᴘʟᴇᴀsᴇ sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴅᴏᴄᴜᴍᴇɴᴛs && ᴠɪᴅᴇᴏ ᴀɴᴅ ᴇɴᴛᴇʀ ɴᴇᴡ ғɪʟᴇ ɴᴀᴍᴇ ᴛᴏ ʀᴇɴᴀᴍᴇ ɪᴛ  
	reply_markup=InlineKeyboardMarkup(
	 [[ InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ 🇮🇳" ,url="https://t.me/Index_AC") ], 
	[InlineKeyboardButton("ᴏᴡɴᴇʀ 🥷", url="https://t.me/SexyNano") ]  ]))
	         



@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       update_channel = CHANNEL
       user_id = message.from_user.id
       if update_channel :
       	try:
       		await client.get_chat_member(update_channel, user_id)
       	except UserNotParticipant:
       		await message.reply_text("**__ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ sᴜʙsᴄʀɪʙᴇ ᴍʏ ᴄʜᴀɴɴᴇʟ__** ",
       		reply_to_message_id = message.id,
       		reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ 🇮🇳" ,url=f"https://t.me/{update_channel}") ]   ]))
       		return
       try:
           bot_data = find_one(int(botid))
           prrename = bot_data['total_rename']
           prsize = bot_data['total_size']
           user_deta = find_one(user_id)
       except:
           await message.reply_text("ᴜsᴇ ᴀʙᴏᴜᴛ ᴄᴍᴅ ғɪʀɪ /about")
       try:
       	used_date = user_deta["date"]
       	buy_date= user_deta["prexdate"]
       	daily = user_deta["daily"]
       	user_type = user_deta["usertype"]
       except:
           await message.reply_text("ᴅᴀᴛᴀʙsᴇ ʜᴀs ʙᴇᴇɴ ᴄʟᴇᴀʀᴇᴅ ᴄʟɪᴄᴋ ᴏɴ /start")
           return
           
           
       c_time = time.time()
       
       if user_type=="Free":
           LIMIT = 600
       else:
           LIMIT = 50
       then = used_date+ LIMIT
       left = round(then - c_time)
       conversion = datetime.timedelta(seconds=left)
       ltime = str(conversion)
       if left > 0:       	    
       	await message.reply_text(f"```sᴏʀʀʏ ᴅᴜᴅᴇ ɪᴍ ɴᴏᴛ ᴏɴʟʏ ғᴏʀ ʏᴏᴜ \n ғʟᴏᴏᴅ ᴄᴏɴᴛʀᴏʟ ɪs ᴀᴄᴛɪᴠᴇ sᴏ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ғᴏʀ  {ltime}```",reply_to_message_id = message.id)
       else:
       		# Forward a single message
           		
       		media = await client.get_messages(message.chat.id,message.id)
       		file = media.document or media.video or media.audio 
       		dcid = FileId.decode(file.file_id).dc_id
       		filename = file.file_name
       		value = 2147483648
       		used_ = find_one(message.from_user.id)
       		used = used_["used_limit"]
       		limit = used_["uploadlimit"]
       		expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
       		if expi != 0:
       			today = date_.today()
       			pattern = '%Y-%m-%d'
       			epcho = int(time.mktime(time.strptime(str(today), pattern)))
       			daily_(message.from_user.id,epcho)
       			used_limit(message.from_user.id,0)			     		
       		remain = limit- used
       		if remain < int(file.file_size):
       		    await message.reply_text(f"**sᴏʀʀʏ!** ɪ ᴄᴀɴ'ᴛ ᴜᴘʟᴏᴀᴅ ғɪʟᴇs ᴛʜᴀᴛ ʟᴀʀɢᴇʀ ᴛʜᴀɴ {humanbytes(limit)}. ғɪʟᴇ sɪᴢᴇ ᴅᴇᴛᴇᴄᴛᴇᴅ {humanbytes(file.file_size)}\nᴜsᴇ ᴅᴀɪʟʏ ʟɪᴍɪᴛ {humanbytes(used)} ɪғ ʏᴏᴜ ᴡᴀɴᴛ ʀᴇɴᴀᴍᴇ ʟᴀʀɢᴇ ғɪʟᴇ ᴜᴘɢʀᴀᴅᴇ ʏᴏᴜʀ ᴘʟᴀɴ ",reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("ᴜᴘɢʀᴀᴅᴇ 💰💳",callback_data = "upgrade") ]]))
       		    return
       		if value < file.file_size:
       		    if STRING:
       		        if buy_date==None:
       		            await message.reply_text(f" ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜᴘʟᴏᴀᴅ ᴍᴏʀᴇ ᴛʜᴀɴ {humanbytes(limit)} ᴜsᴇ ᴅᴀɪʟʏ ʟɪᴍɪᴛ {humanbytes(used)} ",reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("ᴜᴘɢʀᴀᴅᴇ 💰💳",callback_data = "upgrade") ]]))
       		            return
       		        pre_check = check_expi(buy_date)
       		        if pre_check == True:
       		            await message.reply_text(f"""__ᴡʜᴀᴛ ɪ ᴅᴏ ᴡɪᴛʜ ᴛʜɪs ғɪʟᴇ?__\n**ғɪʟᴇ ɴᴀᴍᴇ** :- ```{filename}```\n**ғɪʟᴇ sɪᴢᴇ** :- {humanize.naturalsize(file.file_size)}\n**ᴅᴄ ɪᴅ** :- {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 ʀᴇɴᴀᴍᴇ",callback_data = "rename"),InlineKeyboardButton("✖️ ᴄᴀɴᴄᴇʟ",callback_data = "cancel")  ]]))
       		            total_rename(int(botid),prrename)
       		            total_size(int(botid),prsize,file.file_size)
       		        else:
       		            uploadlimit(message.from_user.id,2147483648)
       		            usertype(message.from_user.id,"Free")
	
       		            await message.reply_text(f'ʏᴏᴜʀ ᴘʟᴀɴ ᴇxᴘɪʀᴇᴅ ᴏɴ {buy_date}',quote=True)
       		            return
       		    else:
       		          	await message.reply_text("ᴄᴀɴ'ᴛ ᴜᴘʟᴏᴀᴅ ʙɪɢɢᴇʀ ᴛʜᴀɴ 𝟸ɢʙ")
       		          	return
       		else:
       		    if buy_date:
       		        pre_check = check_expi(buy_date)
       		        if pre_check == False:
       		            uploadlimit(message.from_user.id,2147483648)
       		            usertype(message.from_user.id,"Free")
       		        
       		    filesize = humanize.naturalsize(file.file_size)
       		    fileid = file.file_id
       		    total_rename(int(botid),prrename)
       		    total_size(int(botid),prsize,file.file_size)
       		    await message.reply_text(f"""__ᴡʜᴀᴛ ɪ ᴅᴏ ᴡɪᴛʜ ᴛʜɪs ғɪʟᴇ?__\n**ғɪʟᴇ ɴᴀᴍᴇ** :- ```{filename}```\n**ғɪʟᴇ sɪᴢᴇ** :- {filesize}\n**ᴅᴄ ɪᴅ** :- {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup(
       		[[ InlineKeyboardButton("📝 ʀᴇɴᴀᴍᴇ",callback_data = "rename"),
       		InlineKeyboardButton("✖️ ᴄᴀɴᴄᴇʟ",callback_data = "cancel")  ]]))
       		
