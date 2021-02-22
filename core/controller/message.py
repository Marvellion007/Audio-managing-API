import sys
sys.path.append("../..")
sys.path.append("..")
from typing import List
from fastapi import HTTPException, Depends, APIRouter
from core.service import message
from core.models import table, base
from pydantic import constr
from sqlalchemy.orm import Session
from datetime import datetime
from typing import Dict

router = APIRouter()

def get_db():
    db = message.a
    try:
        yield db
    finally:
        db.close()        

@router.post("/{audioFileType}")
def create_message(audioFileType: str, audioFileMetadata: dict, db: Session = Depends(get_db)):
    Message_obj = base.createbase(audioFileType = audioFileType, audioFileMetadata = audioFileMetadata )
    result = message.get_message(db,audioFileType=audioFileType, audioFileID=audioFileMetadata["ID"]) 
    if result is None:
        given_date = audioFileMetadata["UPLOAD_TIME"]
        date_format = "%Y-%m-%d %H:%M:%S"
        given = datetime.strptime(given_date, date_format)
        now =  datetime.now()
        if audioFileType.lower()=='"song"':
            if len(audioFileMetadata["NAME"])>100:
                raise HTTPException(status_code=400, detail="Name length exeeded")
            if audioFileMetadata["DURATION"]<0:
                raise HTTPException(status_code=400, detail="duration cannot be negetive")
            if given<now:
                raise HTTPException(status_code=400, detail="date cannot be in past")  
        if audioFileType.lower()=='"podcast"':
            if len(audioFileMetadata["NAME"])>100:
                raise HTTPException(status_code=400, detail="Name length exeeded")
            if audioFileMetadata["DURATION"]<0:
                raise HTTPException(status_code=400, detail="duration cannot be negetive")
            if "HOST" not in audioFileMetadata.keys():
                raise HTTPException(status_code=400, detail="invalid request")
            if len(audioFileMetadata["HOST"])>100:
                raise HTTPException(status_code=400, detail="Host length exeeded")
            if given<now:
                raise HTTPException(status_code=400, detail="date cannot be in past")  
            if audioFileMetadata["PARTICIPANTS"]:
                if not isinstance(audioFileMetadata["PARTICIPANTS"], list):
                    raise HTTPException(status_code=400, detail="participants should be of list type")
        if audioFileType.lower()=='"audiobook"':
            if len(audioFileMetadata["TITLE"])>100:
                raise HTTPException(status_code=400, detail="Title length exeeded")
            if len(audioFileMetadata["AUTHOR"])>100:
                raise HTTPException(status_code=400, detail="Author length exeeded")
            if len(audioFileMetadata["NARRATOR"])>100:
                raise HTTPException(status_code=400, detail="Title length exeeded")
            if audioFileMetadata["DURATION"]<0:
                raise HTTPException(status_code=400, detail="duration cannot be negetive")
            if given<now:
                raise HTTPException(status_code=400, detail="date cannot be in past")  
        result = message.create_message(db, Message_obj)
        return result
    else:
        raise HTTPException(status_code=400, detail="id already there")

@router.get("/{audioFileType}/{audioFileID}")
def read_message(audioFileType: str, audioFileID: int, db: Session = Depends(get_db)) :
    result = message.get_message(db,audioFileType=audioFileType, audioFileID=audioFileID)
    if result is None:
        raise HTTPException(status_code=400, detail="id not found")
    print(result)
    return result

@router.patch("/{audioFileType}/{audioFileID}")
def update_message(audioFileType: str, audioFileMetadata: dict, db: Session = Depends(get_db)):
    Message_obj = base.createbase(audioFileType = audioFileType, audioFileMetadata = audioFileMetadata )
    result = message.get_message(db,audioFileType=audioFileType, audioFileID=audioFileMetadata["ID"])
    if result is None:
        raise HTTPException(status_code=400, detail="id not found")
    given_date = audioFileMetadata["UPLOAD_TIME"]
    date_format = "%Y-%m-%d %H:%M:%S"
    given = datetime.strptime(given_date, date_format)
    now =  datetime.now()
    if audioFileType.lower()=='"song"':
        if len(audioFileMetadata["NAME"])>100:
            raise HTTPException(status_code=400, detail="Name length exeeded")
        if audioFileMetadata["DURATION"]<0:
            raise HTTPException(status_code=400, detail="duration cannot be negetive")
        if given<now:
            raise HTTPException(status_code=400, detail="date cannot be in past")  
    if audioFileType.lower()=='"podcast"':
        if len(audioFileMetadata["NAME"])>100:
            raise HTTPException(status_code=400, detail="Name length exeeded")
        if audioFileMetadata["DURATION"]<0:
            raise HTTPException(status_code=400, detail="duration cannot be negetive")
        if "HOST" not in audioFileMetadata.keys():
            raise HTTPException(status_code=400, detail="invalid request")
        if len(audioFileMetadata["HOST"])>100:
            raise HTTPException(status_code=400, detail="Host length exeeded")
        if given<now:
            raise HTTPException(status_code=400, detail="date cannot be in past")  
        if audioFileMetadata["PARTICIPANTS"]:
            if not isinstance(audioFileMetadata["PARTICIPANTS"], list):
                raise HTTPException(status_code=400, detail="participants should be of list type")
    if audioFileType.lower()=='"audiobook"':
        if len(audioFileMetadata["TITLE"])>100:
            raise HTTPException(status_code=400, detail="Title length exeeded")
        if len(audioFileMetadata["AUTHOR"])>100:
            raise HTTPException(status_code=400, detail="Author length exeeded")
        if len(audioFileMetadata["NARRATOR"])>100:
            raise HTTPException(status_code=400, detail="Title length exeeded")
        if audioFileMetadata["DURATION"]<0:
            raise HTTPException(status_code=400, detail="duration cannot be negetive")
        if given<now:
            raise HTTPException(status_code=400, detail="date cannot be in past")  
    result = message.update_message(db, Message_obj)
    return result  

@router.delete("/{audioFileType}/{audioFileID}")
def delete_message(audioFileType: str, audioFileID: int, db: Session = Depends(get_db))-> str:
    result = message.get_message(db,audioFileType=audioFileType, audioFileID=audioFileID)
    if result is None:
        raise HTTPException(status_code=400, detail="id not found")
    return message.delete_message(db,audioFileType=audioFileType, audioFileID=audioFileID)

