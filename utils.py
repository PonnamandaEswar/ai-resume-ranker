# utils.py

import PyPDF2

def extract_text_from_jd(file):
    filename = file.name.lower()

    try:
        if filename.endswith('.pdf'):
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text() or ''
            return text.strip()

        elif filename.endswith('.txt'):
            return file.read().decode("utf-8").strip()

        else:
            return ""
    except:
        return ""
