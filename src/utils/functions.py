from contextlib import contextmanager
import fitz

@contextmanager
def open_pdf(pdf_contents: bytes):
    doc = fitz.open(stream=pdf_contents, filetype="pdf")
    try:
        yield doc
    finally:
        doc.close()


