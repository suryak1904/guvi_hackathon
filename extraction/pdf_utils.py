import pdfplumber
import fitz
import pytesseract
from pdf2image import convert_from_path
from extraction.text_utils import clean_text


def extract_pdf(path):
    text = _pdfplumber(path)

    if _too_short(text):
        text = _pymupdf(path)

    if _too_short(text):
        text = _ocr(path)

    return clean_text(text)


def _pdfplumber(path):
    text = ""
    try:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception:
        pass
    return text


def _pymupdf(path):
    text = ""
    try:
        doc = fitz.open(path)
        for page in doc:
            text += page.get_text()
    except Exception:
        pass
    return text


def _ocr(path):
    text = ""
    try:
        images = convert_from_path(path)
        for img in images:
            text += pytesseract.image_to_string(img)
    except Exception:
        pass
    return text


def _too_short(text):
    return len(text.strip()) < 200
