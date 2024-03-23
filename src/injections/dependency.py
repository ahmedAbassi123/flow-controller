from src.services.flow_controller_service import FlowService
from src.exceptions.custom_exceptions import NotAPDFError
from src.utils.abstract_classes import Check

class check_file_type(Check):
    def __init__(self, filename: str):
        self.filename=filename
    
    def is_pdf(self)->bool:
        if not self.filename.lower().endswith('.pdf'):
            raise NotAPDFError()
        return True


class PdfServiceFactory:
    @staticmethod
    def create_pdf_flow(contents: bytes):
        return FlowService(contents)
    
    @staticmethod
    def create_pdf_checker(filename: str):
        return check_file_type(filename) 


pdf_service_factory = PdfServiceFactory()
