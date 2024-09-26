
class PDFProcessingError(Exception):
    def __init__(self, detail="Error analyzing PDF"):
        self.detail = detail
        super().__init__(self.detail)

class NotAPDFError(Exception):
    def __init__(self, detail="File is not a PDF"):
        self.detail = detail
        super().__init__(self.detail)

class MixedPDFError(Exception):
    def __init__(self, detail="Mixed PDF not accepted"):
        self.detail = detail
        super().__init__(self.detail)



    


