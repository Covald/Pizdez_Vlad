import random

from utils import config, save_config
import pyrogram

ME_CHAT = 926836636

VOVA_PROC_CHANCE: int = 0
ALL_PROC_CHANCE: int = 0

svetloe = -1001947538282

TEST_CHAT = -1002001629088

andecdot_list = ["https://www.youtube.com/watch?v=k5vSmYlvMb0&ab_channel=ATVPlus",
                 "https://www.youtube.com/watch?v=jrHXEYWXI04&ab_channel=%D0%9C%D0%B8%D1%85%D0%B0",
                 "https://www.youtube.com/watch?v=f-JoX1Eb0dI&ab_channel=ATVPlus",
                 "Попроси Вову!",
                 "https://www.youtube.com/watch?v=xEnwTnPHDi4&ab_channel=PROKTAR",
                 "https://www.youtube.com/watch?v=uSUT2STC4LE&ab_channel=maXXas"
                 ]

goida_files = {
    "photo": "AgACAgIAAxkBAAIBCGcAAcIZatamckc0iHPz4q8llHjazwAC-NoxG_onCEgpxj0e-XIEtQAIAQADAgADbQAHHgQ",
    "animation": "CgACAgIAAxkBAAIBDGcAAcLGExO74XlHqlId_FbxIWYjBgACH00AAvonCEg7m2jwHXQaBx4E"
}


def load_config():
    global VOVA_PROC_CHANCE
    global ALL_PROC_CHANCE
    VOVA_PROC_CHANCE = int(config.get("vova_proc_chance", 0))
    ALL_PROC_CHANCE = int(config.get("all_proc_chance", 0))


load_config()


async def change_proc_chance(message: pyrogram.types.Message, param_name: str, param_value: str):
    global config
    try:
        value = str(int(param_value))
    except Exception as err:
        await message.reply("Pls, sobaka ti sutulaya, use int parameter.")
        return

    config[param_name] = value
    load_config()
    save_config()

    await message.reply(f"Okay, now chances for answers\n"
                        f"all_proc_chance - {ALL_PROC_CHANCE}%.\n"
                        f"vova_proc_chance - {VOVA_PROC_CHANCE}%.")


async def change_proc_chance_vova(client: pyrogram.Client, message: pyrogram.types.Message):
    _message = message.text.split()

    if len(_message) == 1:
        await message.reply(str(VOVA_PROC_CHANCE))
        return

    await change_proc_chance(message, "vova_proc_chance", _message[1])


async def change_proc_chance_all(client: pyrogram.Client, message: pyrogram.types.Message):
    _message = message.text.split()

    if len(_message) == 1:
        await message.reply(str(ALL_PROC_CHANCE))
        return

    await change_proc_chance(message, "all_proc_chance", _message[1])


async def get_chat(client: pyrogram.Client, message: pyrogram.types.Message):
    await client.send_message(926836636, f"{message.chat.username or message.chat.title} - {message.chat.id}")


async def process_message(client: pyrogram.Client, message: pyrogram.types.Message) -> list:
    print(f"Receive message from {message.chat.username or message.chat.title} - {message.text}")
    replaced_symbols = [",", ".", "?", "!", ":", ";"]

    if not message.text:
        return
    
    _message = message.text.lower().strip()
    for symbol in replaced_symbols:
        _message = _message.replace(symbol, " ")
    words = _message.split()
    
    if message.from_user and random.random() <= VOVA_PROC_CHANCE / 100 and message.from_user.username == "@torchCat":
        await message.reply("Хрю-хрю")

    if (("наконец-то" in words or "наконец то" in words or "наконецто" in words) and len(words) == 1) or (("наконец" in words and "то" in words) and len(words) == 2):
        await message.reply("Гойда!")
        await message.reply_photo(goida_files["photo"])
        await message.reply_animation(goida_files["animation"])

    if "гойда" in words or "гойду" in words:
        await message.reply_animation(goida_files["animation"])

    if random.random() >= ALL_PROC_CHANCE / 100:
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
