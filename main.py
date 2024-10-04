# import asyncio
from aiogram import Bot, Dispatcher, executor, types
import logging
from decouple import config

"""
name:   ΔҟΞλ
id:     @AKEL12_bot
link:   https://t.me/AKEL12_bot
github: https://github.com/DrokiGame12/M3
"""

HI_ID = 'CAACAgIAAxkBAAEM6tlm_5dP-XEkVoIRU3dOt5iQcu_1yAACVAADQbVWDGq3-McIjQH6NgQ'

token = config('BOT_TOKEN')
bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def echo_handler(message: types.Message):
    await message.answer_sticker(HI_ID)
    await message.answer(f'HI {message.from_user.first_name}!\nI\'m Akel\'s bot!')

@dp.message_handler()
async def square_number(message):
    text: str = message.text
    if text.isdigit() or (text[0] == '-' and text[1:].isdigit()):
        text: int = int(text)**2
    await message.answer(text)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp)