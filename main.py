import json
import os

import pyrogram
from pyrogram.handlers import MessageHandler

import handlers
from pyrogram import Client, filters

if os.getenv("API_ID") is None:
    from dotenv import load_dotenv

    load_dotenv(".env")

app = Client(
    "my_bot",
    # "my_account",
    api_id=os.getenv("API_ID"),
    api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
)

ME_USER_FILTER = filters.user("@Covald")
VOVA_USER = filters.user("@torchcat")

ME_PRIVATE_CHAT = filters.chat(926836636)
SVETLOE = filters.chat(handlers.svetloe)
TEST_CHAT = handlers.TEST_CHAT


app.add_handler(MessageHandler(handlers.change_proc_chance_vova, filters.command("vova_proc_chance") & ME_PRIVATE_CHAT))

app.add_handler(MessageHandler(handlers.change_proc_chance_all, filters.command("all_proc_chance") & ME_PRIVATE_CHAT))
# app.add_handler(MessageHandler(handlers.vova_answer, SVETLOE & VOVA_USER))

app.add_handler(MessageHandler(handlers.process_message, ~filters.private & filters.chat(TEST_CHAT)))

app.add_handler(MessageHandler(handlers.get_chat, filters.command("get_chat") & ME_USER_FILTER))
app.run()
