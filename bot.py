import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6295603578:AAEICCTRwjkxDiJ-yb0mo_F2EYC-BmgX3Nc")

API_ID = int(os.environ.get("API_ID", "16743442"))

API_HASH = os.environ.get("API_HASH", "12bbd720f4097ba7713c5e40a11dfd2a")

STRING = os.environ.get("STRING", "BQCYTlB43Yr8ZFSjrqionPjgMHvpB-NM1yg6reUzV9cJauK2gEg18LT-KdrrqWjtfYNMjD89bLvV-2apw-0ygZI4oeNBE1NeKc7_X0k8JR7tRVtTqan8OY3CkOaqYu3_asRDRAt4XhpbIoU1De3rWddwMCmrYE-WfaKZ7G-SsOAMKMxL1606rPezl7iGgqFPENgltSONEPfxWMAhQ2IpamiUQcHbpfAGCe1Mnb8TA1Zdpdn2BCy4KPiwO9JP9unqGTWk_UwPKkFLRtT6ggIzSpHbK1DUn3pUAHxZsZ-Iqxqh6hH0aGIjMCLrozWbrsSJFT_aEz7faR5cgZ2pTGg3CHDjAAAAAXd1EakA")


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
