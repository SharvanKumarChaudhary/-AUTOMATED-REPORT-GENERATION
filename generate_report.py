import os
import fitz 
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def read_pdf_text(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def generate_pdf_report(text, output_path):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    text_object = c.beginText(40, height - 50)
    text_object.setFont("Helvetica-Bold", 14)
    text_object.textLine("Automated Report (from PDF)")
    text_object.setFont("Helvetica", 10)
    text_object.textLine("-" * 80)

    lines = text.splitlines()
    y = height - 80
    for line in lines:
        if y <= 50:
            c.drawText(text_object)
            c.showPage()
            text_object = c.beginText(40, height - 50)
            text_object.setFont("Helvetica", 10)
            y = height - 80
        text_object.textLine(line)
        y -= 12

    c.drawText(text_object)
    c.save()
pdf_input = r"C:\\Users\\USER\\Downloads\\python .pdf"
pdf_output = r"C:\\Users\\USER\\OneDrive\\เอกสาร\\generated_report.pdf"

if not os.path.exists(pdf_input):
    print(f"File not found: {pdf_input}")
else:
    content = read_pdf_text(pdf_input)
    generate_pdf_report(content, pdf_output)
    print("Report Generated Successfully!")

    try:
        os.startfile(pdf_output)
    except Exception as e:
        print("Could not open the file automatically:", e)
