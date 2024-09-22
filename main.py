import os
import random
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

proc_chance = config.getint("base", "proc_chance")
# admin_list = config["admin_list"]
print(proc_chance)
app = Client(
    "my_bot",
    # "my_account",
    api_id=os.getenv("API_ID"), api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
)

svetloe = -1001947538282

andecdot_list = ["https://www.youtube.com/watch?v=k5vSmYlvMb0&ab_channel=ATVPlus",
                 "https://www.youtube.com/watch?v=jrHXEYWXI04&ab_channel=%D0%9C%D0%B8%D1%85%D0%B0",
                 "https://www.youtube.com/watch?v=f-JoX1Eb0dI&ab_channel=ATVPlus",
                 "Попроси Вову!",
                 "https://www.youtube.com/watch?v=xEnwTnPHDi4&ab_channel=PROKTAR",
                 "https://www.youtube.com/watch?v=uSUT2STC4LE&ab_channel=maXXas"
                 ]


@app.on_message(filters.chat([svetloe, ]) & filters.text)
async def pizdez_vlad(client, message):
    # Added 10 percent prb of replying
    message_len = len(message.text.split())
    first_word = message.text.split()[0].lower().strip()
    last_word = message.text.split()[-1].lower().strip()
    global proc_chance
    if random.randrange(0, 100, 1) <= proc_chance:

        if "пиздец" in first_word and message_len == 1:
            await message.reply("Влад")
        elif "да" in last_word:
            await message.reply("Пизда.")
        elif "нет" in last_word:
            await message.reply("Ты знаешь чей ответ.")
        elif "пизда" in first_word and message_len == 1:
            await message.reply("Пиздец")
        elif "влад" == first_word and message_len == 1:
            await message.reply("да")

    if "блядство" in first_word and message_len == 1:
        await message.reply("Полностью поддерживаю!")
    if "вот такая есть" in message.text.lower().strip() and message_len == 3:
        await message.reply("Ахвахвххва, ебанько!")
    if "хочу анекдот" in message.text.lower().strip() and message_len == 2:
        await message.reply("".join(random.choices(andecdot_list)))


@app.on_message(filters.command(["chat_list", ]) & filters.text & filters.private)
async def get_chats(client: pyrogram.Client, message):
    _chats = []
    async for i in client.get_dialogs():
        _chats.append((i.chat.id, i.chat.title))
    message.reply("\n".join(map(lambda x: str(x[0]) + " - " + str(x[1]), _chats)))


@app.on_message(filters.command(["change_proc_chance", ]) & filters.text & filters.private)
async def get_chats(client: pyrogram.Client, message: pyrogram.types.Message):
    _message = message.text.split()
    global config
    print(_message)
    if "change_proc_chance" in _message[0]:
        try:
            value = str(int(_message[1]))
        except Exception as err:
            await message.reply("Pls, sobaka ti sutulaya, use int parameter.")
            return
        config.set("base", "proc_chance", value)

    global proc_chance
    proc_chance = config.getint("base", "proc_chance")
    await message.reply(f"Okay, now chance for answer is {proc_chance}%.")
    with open("config.ini", "w") as fp:
        config.write(fp)


app.run()
