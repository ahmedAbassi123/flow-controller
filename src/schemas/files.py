from pydantic import BaseModel
from enum import Enum
from src.utils.validation import PDFTypeEnum

class PDFFile(BaseModel):
    file: bytes




class PDFType(BaseModel):
    Type: PDFTypeEnum