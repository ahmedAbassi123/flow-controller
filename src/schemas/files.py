from pydantic import BaseModel
from src.utils.validation import PDFTypeEnum

class PDFType(BaseModel):
    Type: PDFTypeEnum