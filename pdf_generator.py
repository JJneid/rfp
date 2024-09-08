from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_pdf(analysis_result):
    doc = SimpleDocTemplate("rfp_analysis.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Add title
    elements.append(Paragraph("RFP Analysis Report", styles['Title']))
    elements.append(Spacer(1, 12))

    # Add summary
    elements.append(Paragraph("Summary:", styles['Heading2']))
    elements.append(Paragraph(analysis_result['summary'], styles['BodyText']))
    elements.append(Spacer(1, 12))

    # Add numbers and tables
    elements.append(Paragraph("Key Numbers:", styles['Heading2']))
    data = [['Metric', 'Value']] + list(analysis_result['numbers'].items())
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(table)
    elements.append(Spacer(1, 12))

    # Add objective and target
    elements.append(Paragraph("Objective:", styles['Heading2']))
    elements.append(Paragraph(analysis_result['objective'], styles['BodyText']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph("Target:", styles['Heading2']))
    elements.append(Paragraph(analysis_result['target'], styles['BodyText']))

    # Build the PDF
    doc.build(elements)
    return "rfp_analysis.pdf"
