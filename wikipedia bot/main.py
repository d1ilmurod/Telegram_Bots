from aiogram import types,Bot,Dispatcher,executor
from config import API_TOKEN
from aiogram.types import ParseMode
import wikipedia
import logging


wikipedia.set_lang('uz')
logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN,parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(msg: types.Message):
    await msg.answer("Wikipedia Botga Xush kelibsiz\nQidirmoqchi bo'lgan matnni yuboring")

@dp.message_handler(commands=['help'])
async def help_handler(msg: types.Message):
    await msg.answer("Botda quydagi buyruqlar bor\n"
                     "/start - Botni ishga tushurish\n"
                     "/help - Yordam")


@dp.message_handler()
async def wikipedia_handler(msg: types.Message):
    try:
        matn = msg.text
        malumot = wikipedia.summary(matn)
        await msg.answer(malumot)
    except:
        await msg.answer('Bunday malumot topilmadi')




if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)