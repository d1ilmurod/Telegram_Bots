import valuta
from aiogram import types,Bot,Dispatcher,executor
from config import API_TOKEN

import logging


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN,parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_handler(msg: types.Message):
    await msg.answer("Valuta bot\n"
                     "Tarjima qilmoqchi matnni yuboring")


@dp.message_handler(commands=['help'])
async def help_handler(msg: types.Message):
    await msg.answer("Botda quydagi buyruqlar mavjud\n"
                     "/start - Botni ishga tushurish\n"
                     "/help - Yordam")


@dp.message_handler()
async def valuta_handler(msg :types.Message):
    matn = msg.text
    await msg.answer(valuta.USD.convert_to_currency_units(int(matn)))


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)


