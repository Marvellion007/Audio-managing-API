import sys
sys.path.append("../..")
sys.path.append("..")
from core.repository import message
from core.models import table, base

a=message.SessionLocal()

def get_message(db: message.Session, audioFileType:str, audioFileID: int):
    return message.get_message(db, audioFileType, audioFileID)
    

def create_message(db: message.Session, message_obj: base.createbase):
    return message.create_message(db, message_obj)

def update_message(db: message.Session, message_obj: base.createbase):
    return message.update_message(db, message_obj)
    
def delete_message(db: message.Session, audioFileType:str, audioFileID: int):
    return message.delete_message(db, audioFileType, audioFileID)
