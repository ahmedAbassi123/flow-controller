from fastapi import APIRouter, UploadFile, File, HTTPException, status
from src.injections.dependency import pdf_service_factory
from src.exceptions.custom_exceptions import PDFProcessingError, NotAPDFError
from src.schemas.files import PDFType
import logging

flow_router = APIRouter()

logging.basicConfig(level=logging.DEBUG)  

@flow_router.post('/files/flow/{user_id}', status_code=200)
async def analyze_pdf(user_id: int, pdf_file: UploadFile = File(...)):
    try:
        pdf_checker = pdf_service_factory.create_pdf_checker(pdf_file.filename)
        if not pdf_checker:
            raise NotAPDFError("File is not a PDF")
        
        contents = await pdf_file.read() 
        
        pdf_type = pdf_service_factory.create_pdf_flow(contents)
        if not pdf_type.is_scanned_pdf():
            return PDFType(Type="NOT_SCANNED")
        else: 
            return PDFType(Type="SCANNED")
            
    except PDFProcessingError as e:
        raise HTTPException(status_code=status.HTTP_102_PROCESSING, detail=str(e))
    
    except NotAPDFError as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



    


















    