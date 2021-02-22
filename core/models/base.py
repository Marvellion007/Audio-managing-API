from pydantic import BaseModel
from datetime import datetime

   
class createbase(BaseModel):
    audioFileType: str
    audioFileMetadata: dict

    class Config:
        orm_mode = True

class base(BaseModel):
    audioFileType: str
    audioFileID: int

    class Config:
        orm_mode = True