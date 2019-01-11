from sqlalchemy import create_engine
from conf import DB_FILENAME, LOG_FILENAME, LOG_DIRECTORY, ADMIN_IDS
import os
from db_map import Base, Users
from sqlalchemy.orm import scoped_session, sessionmaker

#Создаем папку для лога
if not os.path.exists(LOG_DIRECTORY):
    os.makedirs(LOG_DIRECTORY)

#Создаем файл для лога
if not os.path.isfile(f'./{LOG_FILENAME}'):
    f = open(LOG_FILENAME, 'w+')

#Настрйока для SQLite3
engine = create_engine(f'sqlite:///{DB_FILENAME}')

#Создаем файл для базы данных
if not os.path.isfile(f'./{DB_FILENAME}'):
    Base.metadata.create_all(engine)

    #Заполнение базы справочниками
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)

    # Закрываем сессию
    Session.close()