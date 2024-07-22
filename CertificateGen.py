from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.colors import HexColor
from io import BytesIO
from datetime import datetime
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
import pandas as pd

def create_overlay(name, date):
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=landscape(A4))
    
    pdfmetrics.registerFont(TTFont('Great Vibes', 'Font/GreatVibes-Regular.ttf'))
    can.setFont("Great Vibes", 40)
    
    text_width = pdfmetrics.stringWidth(name, "Great Vibes", 40)
    page_width, page_height = landscape(A4)
    x_position = (page_width - text_width) / 2
    y_position = 290
    
    can.setFillColor(HexColor('#555553'))
    can.drawString(x_position, y_position, name)

    can.setFont("Helvetica", 12)
    can.drawString(page_width - 260, 263, date)
    
    can.save()
    packet.seek(0)
    return packet

def add_text_to_pdf(template_path, output_path, name, date):
    overlay = create_overlay(name, date)
    overlay_pdf = PdfReader(overlay)
    template_pdf = PdfReader(open(template_path, "rb"))

    writer = PdfWriter()

    for page in template_pdf.pages:
        page.merge_page(overlay_pdf.pages[0])
        writer.add_page(page)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "wb") as output_pdf:
        writer.write(output_pdf)

if __name__ == "__main__":
    csv_file = "Input/attendees.csv" 
    data = pd.read_csv(csv_file)
    names = (data['First name'] + ' ' + data['Last name']).str.title()
    date = str(datetime.now().day) + " / " + str(datetime.now().month) + " / " + str(datetime.now().year)
    template_path = "Template/certificate.pdf"
    for name in names:
        print(name)
        output_path = f"Output/{name.replace(' ', '_')}_certificate.pdf"
        add_text_to_pdf(template_path, output_path, name, date)
