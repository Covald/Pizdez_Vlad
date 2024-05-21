import os

from dotenv import load_dotenv
from pyrogram import Client, filters

load_dotenv(".env")

app = Client(
    "my_bot",
    # "my_account",
    api_id=os.getenv("API_ID"), api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
)

svetloe = -1001947538282


@app.on_message(filters.chat([svetloe, ]) & filters.text)
async def pizdez_vlad(client, message):
    _message = message.text.split()[0].lower().strip()
    if "пиздец" in _message and len(message.text.split()) == 1:
        await message.reply("Влад")


# @app.on_message(filters.text & filters.private)
# async def get_chats(client: pyrogram.Client, message):
#     print("test")
#     _chats = []
#     async for i in client.get_dialogs():
#         _chats.append((i.chat.id, i.chat.title))
#     print(_chats)


app.run()
