from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Numeric
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    user_id = Column('user_id', Numeric, unique=True)
    username = Column('username', String(255))
    name = Column('name', String(255))
    referal_count = Column('referal_count', Integer, default=0)

    def __init__(self, user_id, username=None, name=None, referal_count=0):
        self.user_id = user_id
        self.name = name
        self.username = username
        self.referal_count = referal_count


class Chats(Base):
    __tablename__ = 'Chats'
    id = Column(Integer, primary_key=True)
    chat_id = Column('chat_id', Numeric, unique=True)
    name = Column('name', String(255))

    def __init__(self, chat_id, name=None):
        self.chat_id = chat_id
        self.name = name