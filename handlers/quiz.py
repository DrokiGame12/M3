from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
import os


async def quiz_1(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button = InlineKeyboardButton('Далее', callback_data='quiz_2')

    keyboard.add(button)

    question = 'BMW or Mersedes or Audi'

    answer = ['BMW', "Mersedes", "Audi"]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Ауди лучше!',
        open_period=20,
        reply_markup=keyboard
    )

async def quiz_2(call: types.CallbackQuery):
    question = 'Сколько хромосом у человека'
    answer = ['54', '67', '46', '15']

    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button = InlineKeyboardButton('Далее', callback_data='quiz_3')
    keyboard.add(button)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Ну ну)',
        open_period=20,
        reply_markup=keyboard
    )

async def quiz_3(call: types.CallbackQuery):
    question = 'Как бросить яйцо на бетонный пол, так, чтобы не разбить его?'
    answers = ['Никак, точно разобьется', 'Повернуть яйцо', 'Как хочешь, не разобьется', 'Не знаю']
    photo_path = os.path.join("images", "broken_egg.jpg")

    with open(photo_path, "rb") as photo:
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=photo,
        )
    await bot.send_poll(
        chat_id = call.from_user.id,
        question = question,
        options = answers,
        is_anonymous = False,
        type = 'quiz',
        correct_option_id = 2,
        explanation = 'Бросай. Бетонный пол не треснет. =]',
        open_period = 15
    )
    

def register_handlers_quiz(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2, text='quiz_2')
    dp.register_callback_query_handler(quiz_3, text='quiz_3')