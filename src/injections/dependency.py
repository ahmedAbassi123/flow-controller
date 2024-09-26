from src.services.flow_controller_service import flow_service,FlowService
from src.exceptions.custom_exceptions import NotAPDFError
from src.utils.functions import is_pdf



class PdfServiceFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_pdf_flow()-> FlowService:
        return flow_service
    
    @staticmethod
    def is_pdf(filename:str)->bool:
        if not filename.lower().endswith('.pdf'):
            return False
        return True



pdf_service_factory = PdfServiceFactory()
