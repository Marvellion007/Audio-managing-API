import sys
sys.path.append("../..")
sys.path.append("..")
from sqlalchemy.orm import Session
from core.models import table, base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path
from dotenv import load_dotenv
import os


env_path = Path('config/.env')
load_dotenv(dotenv_path=env_path)
Postgres_user = os.getenv("POSTGRES_USER")
Postgres_password = os.getenv("POSTGRES_PASSWORD")
Postgres_db = os.getenv("POSTGRES_DB")
host = os.getenv("host")

cred = f"{Postgres_user}:{Postgres_password}@{host}/{Postgres_db}"
SQLALCHEMY_DATABASE_URL = f"postgresql://{cred}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False , bind=engine)



if "pytest" not in sys.modules:
    table.Base.metadata.create_all(bind=engine)

def get_message(db: Session, audioFileType:str, audioFileID: int):
    if audioFileType.lower()=="song" or audioFileType.lower()=='"song"' :
        obj= db.query(table.Song).filter(table.Song.ID == audioFileID).first()
        if obj is not None:
            return {"ID": audioFileID,"NAME": obj.NAME, "DURATION": obj.DURATION,"UPLOAD_TIME": obj.UPLOAD_TIME}
        else: 
            return None
    if audioFileType.lower()=="podcast" or audioFileType.lower()=='"podcast"' :
        obj= db.query(table.Podcast).filter(table.Podcast.ID == audioFileID).first()
        if obj is not None:
            return {"ID": audioFileID,"NAME": obj.NAME, "DURATION": obj.DURATION,"UPLOAD_TIME": obj.UPLOAD_TIME, "HOST": obj.HOST, "PARTICIPANTS": obj.PARTICIPANTS}
        else: 
            return None
    if audioFileType.lower()=="audiobook" or audioFileType.lower()=='"audiobook"' :
        obj= db.query(table.Audiobook).filter(table.Audiobook.ID == audioFileID).first()
        if obj is not None:
            return {"ID": audioFileID,"TITLE": obj.TITLE, "AUTHOR": obj.AUTHOR,"UPLOAD_TIME": obj.UPLOAD_TIME, "NARRATOR": obj.NARRATOR, "DURATION": obj.DURATION}
        else: 
            return None

def create_message(db: Session, message: base.createbase):
    db_message=""
    if message.audioFileType.lower()=='"song"' or message.audioFileType.lower()=="song" :
        db_message = table.Song(ID=message.audioFileMetadata["ID"],NAME= message.audioFileMetadata["NAME"], DURATION=message.audioFileMetadata["DURATION"], UPLOAD_TIME=message.audioFileMetadata["UPLOAD_TIME"])
    if message.audioFileType.lower()=='"podcast"' or message.audioFileType.lower()=="podcast" :
        db_message = table.Podcast(ID=message.audioFileMetadata["ID"],NAME= message.audioFileMetadata["NAME"], DURATION=message.audioFileMetadata["DURATION"], UPLOAD_TIME=message.audioFileMetadata["UPLOAD_TIME"], HOST=message.audioFileMetadata["HOST"], PARTICIPANTS=message.audioFileMetadata["PARTICIPANTS"])
    if message.audioFileType.lower()=='"audiobook"' or message.audioFileType.lower()=="audiobook":
        db_message = table.Audiobook(ID=message.audioFileMetadata["ID"],TITLE= message.audioFileMetadata["TITLE"], AUTHOR=message.audioFileMetadata["AUTHOR"], NARRATOR=message.audioFileMetadata["NARRATOR"],  DURATION=message.audioFileMetadata["DURATION"], UPLOAD_TIME=message.audioFileMetadata["UPLOAD_TIME"])
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message 

def update_message(db: Session, message: base.createbase):
    obj=""
    if message.audioFileType.lower()=="song" or message.audioFileType.lower()=='"song"' :
        obj= db.query(table.Song).filter(table.Song.ID == message.audioFileMetadata["ID"]).first()
        obj.NAME= message.audioFileMetadata["NAME"]
        obj.DURATION=message.audioFileMetadata["DURATION"]
        obj.UPLOAD_TIME=message.audioFileMetadata["UPLOAD_TIME"]
    if message.audioFileType.lower()=="podcast" or message.audioFileType.lower()=='"podcast"' :
        obj= db.query(table.Podcast).filter(table.Podcast.ID == message.audioFileMetadata["ID"]).first()
        obj.NAME= message.audioFileMetadata["NAME"]
        obj.DURATION=message.audioFileMetadata["DURATION"]
        obj.UPLOAD_TIME=message.audioFileMetadata["UPLOAD_TIME"]
        obj.HOST=message.audioFileMetadata["HOST"]
        if message.audioFileMetadata["PARTICIPANTS"]:
            obj.PARTICIPANTS=message.audioFileMetadata["PARTICIPANTS"]
    if message.audioFileType.lower()=="audiobook" or message.audioFileType.lower()=='"audiobook"':
        obj= db.query(table.Audiobook).filter(table.Audiobook.ID == message.audioFileMetadata["ID"]).first()
        obj.TITLE= message.audioFileMetadata["TITLE"]
        obj.AUTHOR=message.audioFileMetadata["AUTHOR"]
        obj.NARRATOR=message.audioFileMetadata["NARRATOR"]
        obj.DURATION=message.audioFileMetadata["DURATION"]
        obj.UPLOAD_TIME=message.audioFileMetadata["UPLOAD_TIME"]
    db.commit()
    db.refresh(obj)
    return "ID Updated"

def delete_message(db: Session, audioFileType:str, audioFileID: int):
    if audioFileType.lower()=="song" or audioFileType.lower()=='"song"' :
        obj= db.query(table.Song).filter(table.Song.ID == audioFileID).delete()
    if audioFileType.lower()=="podcast" or audioFileType.lower()=='"podcast"' :
        obj= db.query(table.Podcast).filter(table.Podcast.ID == audioFileID).delete()
    if audioFileType.lower()=="audiobook" or audioFileType.lower()=='"audiobook"':
        obj= db.query(table.Audiobook).filter(table.Audiobook.ID == audioFileID).delete()
    db.commit()
    return "ID deleted"