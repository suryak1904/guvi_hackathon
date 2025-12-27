from docx import Document
from extraction.text_utils import clean_text


def extract_docx(path):
    doc = Document(path)
    text = "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
    return clean_text(text)
