from datetime import datetime

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ContentType, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaDocument
from aiogram.utils import executor
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import asyncio
import logging

from messages import MESSAGES
from conf import LOG_FILENAME, TOKEN, DB_FILENAME, PROXY_AUTH, PROXY_URL

from functions import prettyUsername, is_admin

logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO, filename=LOG_FILENAME)
loop = asyncio.get_event_loop()
bot = Bot(TOKEN, parse_mode=types.ParseMode.HTML, proxy=PROXY_URL,
          proxy_auth=PROXY_AUTH)
dp = Dispatcher(bot, loop=loop, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

engine = create_engine(f'sqlite:///{DB_FILENAME}')

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


@dp.message_handler(commands=['start'], func=lambda message: message.chat.type == 'private')
async def process_start_command(message: types.Message):
    await message.reply(MESSAGES['start'], reply=False)


@dp.message_handler(commands=['help'], func=lambda message: message.chat.type == 'private')
async def process_help_command(message: types.Message):
    await message.reply(MESSAGES['help'], reply=False)


if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown)


