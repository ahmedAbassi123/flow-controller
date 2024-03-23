from abc import ABC, abstractmethod

# Define an abstract class
class Flow(ABC):
    @abstractmethod
    def is_scanned_pdf(self):
        pass

class Check(ABC):
    def is_pdf(self):
        pass