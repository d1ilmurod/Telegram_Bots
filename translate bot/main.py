from aiogram import types,Bot,Dispatcher,executor
from config import API_TOKEN
import logging
from googletrans import Translator


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN,parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
tarjima = Translator()

@dp.message_handler(commands=['start'])
async def start_handler(msg: types.Message):
    await msg.answer("Translate Botga Xush kelibsiz\n"
                     "Tarjima qilmoqchi matnni yuboring")


@dp.message_handler(commands=['help'])
async def start_handler(msg: types.Message):
    await msg.answer("Botda quydagi buyruqlar mavjud\n"
                     "/start - Botni ishga tushurish\n"
                     "/help - Yordam")

@dp.message_handler()
async def get_date(msg: types.Message):
    try:
       matn = msg.text
       tarjimon = tarjima.translate(matn,src = 'uz', dest='en')
       tarjima_qilindi = tarjimon.text
       await msg.reply(tarjima_qilindi)
    except:
        await msg.answer("Uzbekcha so'z kiriting")



if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)


