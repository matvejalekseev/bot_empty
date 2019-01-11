import re

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from messages import MESSAGES
from sqlalchemy import create_engine, and_, func, desc, asc
from sqlalchemy.orm import scoped_session, sessionmaker
from db_map import Users, Chats, Referal
from conf import DB_FILENAME, ADMIN_IDS
from pytz import timezone
from datetime import datetime

engine = create_engine(f'sqlite:///{DB_FILENAME}')
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
UTC = timezone('UTC')


def date_now():
    return datetime.now(UTC).date()


def time_now():
    return datetime.now(UTC)


def is_str(s):
    if s is None or s == 'None' or s == '':
        return False
    else:
        return True


def prettyUsername(n, id):
    try:
        if id:
            user = '<a href="tg://user?id=' + str(round(id)) + '">' + n + '</a>'
        else:
            user = n
        return user
    except:
        return MESSAGES['error']


def is_admin(id):
    if id in ADMIN_IDS:
        return True
    else:
        return False


