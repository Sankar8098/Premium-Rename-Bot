import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6295603578:AAEICCTRwjkxDiJ-yb0mo_F2EYC-BmgX3Nc")

API_ID = int(os.environ.get("API_ID", "16743442"))

API_HASH = os.environ.get("API_HASH", "12bbd720f4097ba7713c5e40a11dfd2a")

STRING = os.environ.get("STRING", "BQBtCcmtxiQNzwe_bnndwMyOQZJ7OXRewlIHruEIR4vwXV11inUHnwO9e7_SC0ipDPt8Wr4Yu0CDBUq5V2DgR_NP0pjBLrAKEYrMbs0x9CVhZdNoKVdXPxUS7cRGBv6cOHc7s06utr38eU9_dhRZr199LDaS9XprpL0dsDcjbCKp8_-uEve4kqKeiaKY3KQngS9VaTUqjswwcsIYzn5lHPBPtK54MMpTkbNGD1R7EMxj35c3Y6G71vwqVd6R7f8ffPhxivM5KDB-CrBvlrRYNERCcp9BHvZ3NYeDBI-T4JIOJRdIHhfR4FyhO2SR0jq83-TBgm5kw6Qz07eyMxHFzD_0AAAAAXd1EakA")


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
