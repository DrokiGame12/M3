# import asyncio
from aiogram import executor
import logging
from config import dp, bot
from handlers import commands, echo, quiz

"""
name:   ΔҟΞλ
id:     @AKEL12_bot
link:   https://t.me/AKEL12_bot
github: https://github.com/DrokiGame12/M3
"""

commands.register_handlers_commands(dp)
quiz.register_handlers_quiz(dp)

echo.register_handlers_echo(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)