from aiogram import types,Bot,Dispatcher,executor
from config import API_TOKEN
import logging
import valuta_api



logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN,parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_handler(msg: types.Message):
    await msg.answer("Assalomu aleykum valuta kurs botga Xush kelibsiz\n")
    await msg.answer(f"Hozir {valuta_api.sana} Sana bilan dollar kursi {valuta_api.kurs} so'mga teng")



@dp.message_handler(commands=['help'])
async def start_handler(msg: types.Message):
    await msg.answer("Botda quydagi buyruqlar mavjud\n"
                     "/start - Botni ishga tushurish\n"
                     "/help - Yordam")


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)


