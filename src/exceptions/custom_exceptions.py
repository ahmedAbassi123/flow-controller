from fastapi import HTTPException


class PDFProcessingError(Exception):
    def __init__(self, detail="Error analyzing PDF"):
        self.detail = detail
        super().__init__(self.detail)


class CustomPDFExtractionError(Exception):
     def __init__(self, detail="Error occurred during PDF extraction: "):
        self.detail = detail
        super().__init__(self.detail)
        

class CustomOCRProcessingError(Exception):
     def __init__(self, detail="Error occurred during OCR processing: "):
        self.detail = detail
        super().__init__(self.detail)
    


