from fastapi import APIRouter, UploadFile, File, HTTPException, status
from src.services.flow_controller_service import FlowService
from src.exceptions.custom_exceptions import PDFProcessingError
from src.schemas.files import PDFStatus
import logging
import io

router = APIRouter()

logging.basicConfig(level=logging.DEBUG)  

@router.post('/files/flow/{document_id}', status_code=200)
async def analyze_pdf(document_id: int, pdf_file: UploadFile = File(...)):
    try:
        contents = await pdf_file.read() 
        flow_service = FlowService(contents)
        
        if not flow_service.is_scanned_pdf():
            return PDFStatus(status="The PDF is not scanned")
        else: 
            return PDFStatus(status="The PDF is scanned")
            
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    


















    