from src.schemas.files import PDFFile
import fitz
from src.exceptions.custom_exceptions import PDFProcessingError,NotAPDFError
from src.schemas.files import PDFType
from src.utils.abstract_classes import Flow
from src.utils.functions import open_pdf


class FlowService(Flow):
    def __init__(self, pdf_contents: bytes):
        self.pdf_contents=pdf_contents

    def is_scanned_pdf(self)->bool:
        try:
            with open_pdf(self.pdf_contents) as doc:
                total_pages = doc.page_count
                num_blank_pages = 0
                for page_num in range(total_pages):
                    page = doc.load_page(page_num)
                    text = page.get_text()
                    if not text.strip():
                        num_blank_pages += 1
                
                if num_blank_pages / total_pages > 0.5:
                    return True  # More than half of the pages are blank (scanned)
                else:
                    return False
            
        except PermissionError:
            raise PDFProcessingError("Permission denied. Make sure you have the necessary permissions to access the file.")
        
        except ValueError:
            raise PDFProcessingError("Invalid PDF contents or unable to open the document.")

       
            
        
            