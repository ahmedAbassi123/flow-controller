from enum import Enum

class PDFTypeEnum(str, Enum):
    SCANNED = "SCANNED"
    NOT_SCANNED = "NOT_SCANNED"