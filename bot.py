import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5964494060:AAFfOEerT8lR8YqyEHJQtbFQidqkqkYUaO8")

API_ID = int(os.environ.get("API_ID", "16743442"))

API_HASH = os.environ.get("API_HASH", "12bbd720f4097ba7713c5e40a11dfd2a")

STRING = os.environ.get("STRING", "BQBKxhVZpv89lKSNTJEcQYo2IHSci8y8GGxPFyA9w0X-4tYswcyy4-o8OZ5C71Hk5Jag3D7_jCJQOhJmRpNlWr81h048vCW0TDWqTjjiBoLVwDmbbBN09HewGTsCcwvwfWQVVSUQ-P4WJZZDHDf0bM0DdYoU-9zO74MUqibRx1ZXsRsVHS1ylguxrqfzxiOfVQfpyUZTto14uH1LfL-sN5n7ZcYCjmGCaO31GXqc3G5FLQdvErE-8MlYlxGLvmkXaU3eE9s0-VRe5p25031R0qgEP2kOCKRfc8ySxlrP33IkU2U9bR8Vk-JHIlpKPI_LoDJw1uTUyeqTVgt8v0te8Tl4AAAAAXF7EUsA")


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
