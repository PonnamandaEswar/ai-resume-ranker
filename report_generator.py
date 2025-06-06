# report_generator.py

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import os

def generate_pdf_report(ranking, resume_names, output_path="output/rank_report.pdf"):
    if not os.path.exists("output"):
        os.makedirs("output")

    doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    title = Paragraph("AI Resume Ranker - Match Score Report", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 20))

    # Table Header
    data = [["Rank", "Resume Name", "Match Score (%)"]]

    # Table Rows
    for rank, (idx, score) in enumerate(ranking, start=1):
        name = resume_names[idx]
        percent = round(score * 100, 2)
        data.append([rank, name, f"{percent}%"])

    # Define table style
    table = Table(data, colWidths=[50, 300, 100])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ]))

    elements.append(table)
    doc.build(elements)
    return output_path
