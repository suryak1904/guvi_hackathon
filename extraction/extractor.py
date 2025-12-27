from extraction.pdf_utils import extract_pdf
from extraction.docx_utils import extract_docx
from extraction.text_utils import extract_txt
from extraction.language import detect_language
from extraction.clause_splitter import split_clauses


def extract_and_split(file_path: str, file_type: str):
    file_type = file_type.lower()

    if file_type == "pdf":
        text = extract_pdf(file_path)
    elif file_type in ["doc", "docx"]:
        text = extract_docx(file_path)
    elif file_type == "txt":
        text = extract_txt(file_path)
    else:
        raise ValueError("Unsupported file type")

    language = detect_language(text)
    clauses = split_clauses(text, language)

    return clauses
