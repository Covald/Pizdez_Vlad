import functools
import os
import random
import typing
from configparser import ConfigParser

import pyrogram
from pyrogram import Client, filters

if os.getenv("API_ID") is None:
    from dotenv import load_dotenv

    load_dotenv(".env")

# instantiate
config = ConfigParser()

# parse existing file
config.read('config.ini')

vova_proc_chance = config.getint("base", "vova_proc_chance")
all_proc_chance = config.getint("base", "all_proc_chance")
# admin_list = config["admin_list"]

app = Client(
    "my_bot",
    # "my_account",
    api_id=os.getenv("API_ID"), api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
)

svetloe = -1001947538282

TEST_CHAT = -4533866272

andecdot_list = ["https://www.youtube.com/watch?v=k5vSmYlvMb0&ab_channel=ATVPlus",
                 "https://www.youtube.com/watch?v=jrHXEYWXI04&ab_channel=%D0%9C%D0%B8%D1%85%D0%B0",
                 "https://www.youtube.com/watch?v=f-JoX1Eb0dI&ab_channel=ATVPlus",
                 "Попроси Вову!",
                 "https://www.youtube.com/watch?v=xEnwTnPHDi4&ab_channel=PROKTAR",
                 "https://www.youtube.com/watch?v=uSUT2STC4LE&ab_channel=maXXas"
                 ]


@app.on_message(filters.command("get_chat") & filters.user("@Covald"))
async def get_chat(client: pyrogram.Client, message: pyrogram.types.Message):
    await client.send_message(926836636, f"{message.chat.username or message.chat.title} - {message.chat.id}")


# @app.on_message(filters.chat(TEST_CHAT)("/who@vkvante_bot"))
# async def whoi(client: pyrogram.Client, message: pyrogram.types.Message):
#     await message.reply("Й")


@app.on_message(filters.chat(svetloe) & filters.user("@torchCat"))
async def vova_answer(client: pyrogram.Client, message: pyrogram.types.Message):
    if random.randrange(0, 100, 1) > vova_proc_chance:
        return
    await message.reply("Хр хр")


@app.on_message(filters.chat([svetloe, ]) & filters.text)
async def pizdez_vlad(client, message: pyrogram.types.Message):
    # Added 10 percent prb of replying
    global all_proc_chance
    if random.randrange(0, 100, 1) > all_proc_chance:
        return
    message_len = len(message.text.split())
    first_word = message.text.split()[0].lower().strip().replace(".", "").replace(",", "")
    last_word = message.text.split()[-1].lower().strip().replace(".", "").replace(",", "")

    if "пиздец" in first_word and message_len == 1:
        await message.reply("Влад")
    elif "да" == last_word[-2:-1].lower():
        await message.reply("Пизда.")
    elif "нет" == last_word.lower():
        await message.reply("Ты знаешь чей ответ.")
    elif "пизда" == first_word[-5:-1].lower():
        await message.reply("Да.")
    elif "блядство" in last_word.lower():
        await message.reply("Полностью поддерживаю!")
    if "вот такая есть" in message.text.lower() and message_len == 3:
        await message.reply("Ахвахвххва, ебанько!")
    if "анекдот" in last_word.lower():
        await message.reply("".join(random.choices(andecdot_list)))


@app.on_message(filters.command(["chat_list", ]) & filters.private & filters.user("@Covald"))
async def get_chats(client: pyrogram.Client, message):
    _chats = []
    async for i in client.get_dialogs():
        _chats.append((i.chat.id, i.chat.title))
    message.reply("\n".join(map(lambda x: str(x[0]) + " - " + str(x[1]), _chats)))


@app.on_message(
    filters.command(["change_proc_chance_for_vova", ]) & filters.text & filters.private & filters.user("@Covald"))
async def change_chanche_for_vova(client: pyrogram.Client, message: pyrogram.types.Message):
    _message = message.text.split()

    if len(_message) == 1:
        await message.reply(vova_proc_chance)
        return

    global config
    try:
        value = str(int(_message[1]))
    except Exception as err:
        await message.reply("Pls, sobaka ti sutulaya, use int parameter.")
        return
    config.set("base", "vova_proc_chance", value)

    global proc_chance
    proc_chance = config.getint("base", "vova_proc_chance")
    await message.reply(f"Okay, now chance for answer is {proc_chance}%.")
    with open("config.ini", "w") as fp:
        config.write(fp)


@app.on_message(
    filters.command(["change_proc_chance_for_all", ]) & filters.text & filters.private & filters.user("@Covald"))
async def get_chats(client: pyrogram.Client, message: pyrogram.types.Message):
    _message = message.text.split()

    if len(_message) == 1:
        await message.reply(all_proc_chance)
        return

    global config
    try:
        value = str(int(_message[1]))
    except Exception as err:
        await message.reply("Pls, sobaka ti sutulaya, use int parameter.")
        return
    config.set("base", "all_proc_chance", value)

    global proc_chance
    proc_chance = config.getint("base", "all_proc_chance")
    await message.reply(f"Okay, now chance for answer is {proc_chance}%.")
    with open("config.ini", "w") as fp:
        config.write(fp)


app.run()
