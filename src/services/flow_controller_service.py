
from src.exceptions.custom_exceptions import PDFProcessingError,NotAPDFError,MixedPDFError
from src.schemas.files import PDFType
from src.utils.abstract_classes import AbstractProcessingFlow
from src.utils.functions import open_pdf


class FlowService(AbstractProcessingFlow):
    def __init__(self):
        pass

    def is_scanned_pdf(self,pdf_contents:bytes)->bool:
        try:
            with open_pdf(pdf_contents) as doc:
                total_pages = doc.page_count
                print(total_pages)
                num_blank_pages = 0
                for page_num in range(total_pages):
                    page = doc.load_page(page_num)
                    text = page.get_text()
                    if not text.strip() : 
                        num_blank_pages += 1
                
                print(num_blank_pages)
                if num_blank_pages==total_pages :
                    return True  
                elif num_blank_pages==0:
                    return False
                else: 
                    raise MixedPDFError()
             
                
        except PermissionError:
            raise PDFProcessingError("Permission denied. Make sure you have the necessary permissions to access the file.")
        
        except ValueError:
            raise PDFProcessingError("Invalid PDF contents or unable to open the document.")
        
flow_service=FlowService()
        
    


       
            
        
            