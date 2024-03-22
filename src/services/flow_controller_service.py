from src.schemas.files import PDFFile
import fitz
import pytesseract
from PIL import Image
from src.exceptions.custom_exceptions import PDFProcessingError
from src.schemas.files import PDFStatus


class FlowService:
    def __init__(self, pdf_contents: bytes):
        self.pdf_contents=pdf_contents

    def is_scanned_pdf(self)->bool:
        try:
            doc = fitz.open(stream=self.pdf_contents,filetype="pdf")
            total_pages = doc.page_count
            num_blank_pages = 0
            for page_num in range(total_pages):
                page = doc.load_page(page_num)
                text = page.get_text()
                if not text.strip():
                    num_blank_pages += 1
            doc.close()
            if num_blank_pages / total_pages > 0.5:
                return True  # More than half of the pages are blank (scanned)
            else:
                return False
            
        except PermissionError:
            raise PDFProcessingError("Permission denied. Make sure you have the necessary permissions to access the file.")
        
        except ValueError:
            raise PDFProcessingError("Invalid PDF contents or unable to open the document.")

       
            
        
            