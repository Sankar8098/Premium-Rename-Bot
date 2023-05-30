import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6295603578:AAEdxq3Nh5zPKMnr-1RfgosDl5Q10Nwj54M")

API_ID = int(os.environ.get("API_ID", "16743442"))

API_HASH = os.environ.get("API_HASH", "12bbd720f4097ba7713c5e40a11dfd2a")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
