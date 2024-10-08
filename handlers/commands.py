from aiogram import types, Dispatcher
from config import bot
import os
from random import choice


HI_ID = 'CAACAgIAAxkBAAEM6tlm_5dP-XEkVoIRU3dOt5iQcu_1yAACVAADQbVWDGq3-McIjQH6NgQ'
async def command_start_handler(message: types.Message):
    name = message.from_user.first_name
    await bot.send_message(
        chat_id = message.from_user.id, 
        text = f'HI {name}!\nI\'m Akel\'s bot!'
    )
    await message.answer_sticker(HI_ID)



async def send_picture_handler(message: types.Message):
    photo_path = os.path.join("images", "cyber_city.jpg")
    with open(photo_path, "rb") as photo:
        await message.answer_photo(
            photo=photo,
            caption="*bold* [ CYBER CITY ]",
            parse_mode = types.ParseMode.MARKDOWN_V2
        )



def game_dice(games: list) -> str:
    '''
    get all games list
    return one random game
    '''
    return choice(games)

async def random_game_handler(message: types.Message):
    games = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']
    await message.answer(game_dice(games))


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(command_start_handler, commands=['start'])
    dp.register_message_handler(send_picture_handler, commands=['pic'])
    dp.register_message_handler(random_game_handler, commands=['game'])