import os
from pypdf import PdfWriter

def merge_pdfs(input_folder, output_name="combined_tugas.pdf"):
    merger = PdfWriter()
    
    files = [f for f in os.listdir(input_folder) if f.lower().endswith(".pdf")]
    files.sort()
    
    for pdf in files:
        path = os.path.join(input_folder, pdf)
        merger.append(path)
        print(f"Menggabungkan: {pdf}")
    
    merger.write(output_name)
    merger.close()
    print(f"\nSelesai! File disimpan sebagai: {output_name}")

if __name__ == "__main__":
    folder = input("Masukkan folder berisi PDF: ")
    merge_pdfs(folder)