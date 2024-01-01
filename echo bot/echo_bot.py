from aiogram import types,Bot,Dispatcher,executor
from config import API_TOKEN
import logging

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("Botga Xush kelibsiz")

@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await message.answer("Botda Quydagi buyruqlar bot\n"
                         "/star - Botni ishga tushurush\n"
                         "/help - yordam")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)