from langdetect import detect


def detect_language(text):
    try:
        return "hi" if detect(text) == "hi" else "en"
    except Exception:
        return "en"
