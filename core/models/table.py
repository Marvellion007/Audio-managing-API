import sys
sys.path.append("../..")
sys.path.append("..")
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()


class Song(Base):
    __tablename__ = "Song"

    ID = Column(Integer, primary_key=True,index=False)
    NAME = Column(String)
    DURATION = Column(Integer)
    UPLOAD_TIME = Column(String)

class Podcast(Base):
    __tablename__ = "Podcast"

    ID = Column(Integer, primary_key=True,index=False)
    NAME = Column(String)
    DURATION = Column(Integer)
    UPLOAD_TIME = Column(String)
    HOST = Column(String)
    PARTICIPANTS = Column(String)

class Audiobook(Base):
    __tablename__ = "Audiobook"

    ID = Column(Integer, primary_key=True,index=False)
    TITLE = Column(String)
    AUTHOR = Column(String)
    NARRATOR = Column(String)
    DURATION = Column(Integer)
    UPLOAD_TIME = Column(String)
