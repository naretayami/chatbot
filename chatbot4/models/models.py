from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime

class studyuser(Base):
    __tablename__ = 'studyusers'
    id = Column(Integer, primary_key=True)
    kamoku = Column(String(128), unique=True)
    kiroku = Column(Text)
    time = column(Text)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, title=None, body=None, date=None):
        self.kamoku = kamoku
        self.kiroku = kiroku
        self.time = time
        self.date = date
        

    def __repr__(self):
        return '<Title %r>' % (self.kamoku)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(128), unique=True)
    hashed_password = Column(String(128))

    def __init__(self, user_name=None, hashed_password=None):
        self.user_name = user_name
        self.hashed_password = hashed_password

    def __repr__(self):
        return '<Name %r>' % (self.user_name)