import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','6049442426:AAFXdX3YnFM7gf1B5u52bbSpO44oWyQGTdo')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"Total User:- {total_user()}\nBot :- @FourGBRename_RoBot\nCreater :- @SexyNano\nLanguage :-Python3\nLibrary :- Pyrogram\nServer :- VPS\nTotal Renamed File :-{total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))} ",quote=True)
