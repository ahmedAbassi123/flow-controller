from abc import ABC, abstractmethod

class AbstractProcessingFlow(ABC):
    
    @abstractmethod
    def is_scanned_pdf(self):
        pass

