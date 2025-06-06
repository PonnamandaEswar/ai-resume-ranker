# resume_parser.py

import docx
import PyPDF2

def extract_text_from_pdf(file):
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text() or ''
        return text.strip()
    except:
        return ""

def extract_text_from_docx(file):
    try:
        doc = docx.Document(file)
        text = '\n'.join([para.text for para in doc.paragraphs])
        return text.strip()
    except:
        return ""

def extract_resume_text(file):
    filename = file.name.lower()
    
    if filename.endswith('.pdf'):
        return extract_text_from_pdf(file)
    elif filename.endswith('.docx'):
        return extract_text_from_docx(file)
    else:
        return ""
