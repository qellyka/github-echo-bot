#https://t.me/gaford_bot
import logging
import os
import dotenv
from aiogram import executor
from aiogram import Bot, Dispatcher, types
dotenv.load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types='text')
async def echo_text(message: types.Message):
    await message.answer(message.text)

@dp.message_handler(content_types='photo')
async def echo_photo(message: types.Message):
    await message.answer_photo(photo=message.photo[-1].file_id)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    executor.start_polling(dp)