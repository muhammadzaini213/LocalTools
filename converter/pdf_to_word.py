from pdfminer.high_level import extract_text
from docx import Document
import os

def pdf_to_word(pdf_path):
    text = extract_text(pdf_path)
    doc = Document()
    doc.add_paragraph(text)
    
    out_name = os.path.splitext(pdf_path)[0] + ".docx"
    doc.save(out_name)
    print(f"Berhasil konversi ke: {out_name}")

if __name__ == "__main__":
    file_pdf = input("Masukkan nama file PDF: ")
    pdf_to_word(file_pdf)