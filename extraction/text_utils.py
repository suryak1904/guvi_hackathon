import re


def extract_txt(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return clean_text(f.read())


def clean_text(text):
    text = re.sub(r"\n\s*\n", "\n", text)
    text = re.sub(r"Page \d+ of \d+", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip()
