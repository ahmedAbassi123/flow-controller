from pydantic import BaseModel

class PDFFile(BaseModel):
    file: bytes


class PDFStatus(BaseModel):
    status:str