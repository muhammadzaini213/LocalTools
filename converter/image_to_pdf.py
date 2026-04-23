import os
import argparse
from PIL import Image

def convert_images_to_pdf(input_folder, output_filename, quality=90):
    extensions = (".jpg", ".jpeg", ".png", ".bmp", ".webp")

    files = [f for f in os.listdir(input_folder) if f.lower().endswith(extensions)]
    files.sort() 

    if not files:
        print(f"Tidak ada gambar ditemukan di folder: {input_folder}")
        return

    image_list = []
    
    print(f"Menemukan {len(files)} gambar. Sedang memproses...")

    for file in files:
        img_path = os.path.join(input_folder, file)
        img = Image.open(img_path)
        
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        elif img.mode != "RGB":
            img = img.convert("RGB")
            
        image_list.append(img)

    if image_list:
        base_img = image_list[0]
        extra_pages = image_list[1:]
        
        base_img.save(
            output_filename, 
            "PDF", 
            save_all=True, 
            append_images=extra_pages, 
            quality=quality
        )
        print(f"Sukses! PDF disimpan di: {output_filename}")

def main():
    parser = argparse.ArgumentParser(description="Gabungkan gambar menjadi satu PDF")
    parser.add_argument("-i", "--input", default="input_images", help="Folder berisi gambar")
    parser.add_argument("-o", "--output", default="hasil_gabungan.pdf", help="Nama file PDF hasil")
    parser.add_argument("-q", "--quality", type=int, default=90, help="Kualitas gambar dalam PDF (1-100)")
    
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Folder '{args.input}' tidak ditemukan!")
        return

    output_name = args.output
    if not output_name.lower().endswith(".pdf"):
        output_name += ".pdf"

    convert_images_to_pdf(args.input, output_name, args.quality)

if __name__ == "__main__":
    main()