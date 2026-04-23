import subprocess
import os
import argparse
import platform

def compress_pdf(input_path, output_path, power=2):
    """
    Fungsi kompresi menggunakan Ghostscript.
    power:
    0: default (kualitas oke)
    1: prepress (kualitas tinggi, 300 dpi)
    2: printer (bagus, 300 dpi)
    3: ebook (menengah, 150 dpi)
    4: screen (kualitas rendah, 72 dpi, ukuran terkecil)
    """
    
    modes = {
        0: "/default",
        1: "/prepress",
        2: "/printer",
        3: "/ebook",
        4: "/screen"
    }
    
    setting = modes.get(power, "/ebook")

    # Perintah Ghostscript
    # Di Windows biasanya namanya 'gswin64c', di Linux 'gs'
    gs_cmd = "gs" if platform.system() != "Windows" else "gswin64c"

    cmd = [
        gs_cmd,
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        f"-dPDFSETTINGS={setting}",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output_path}",
        input_path
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f" Berhasil: {os.path.basename(input_path)} -> {os.path.basename(output_path)}")
    except subprocess.CalledProcessError:
        print(f" Gagal mengompres {input_path}. Pastikan Ghostscript terinstall.")
    except FileNotFoundError:
        print(f" Ghostscript ({gs_cmd}) tidak ditemukan di sistem!")

def main():
    parser = argparse.ArgumentParser(description="PDF Compressor menggunakan Ghostscript")
    parser.add_argument("-i", "--input", default="input_pdf", help="Folder input atau file PDF")
    parser.add_argument("-o", "--output", default="output_pdf", help="Folder hasil kompresi")
    parser.add_argument("-p", "--power", type=int, default=3, help="Level kompresi (0-4). 4 paling kecil.")
    
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    # Cek apakah input itu file atau folder
    if os.path.isfile(args.input):
        out_file = os.path.join(args.output, "compressed_" + os.path.basename(args.input))
        compress_pdf(args.input, out_file, args.power)
        
    elif os.path.isdir(args.input):
        files = [f for f in os.listdir(args.input) if f.lower().endswith(".pdf")]
        if not files:
            print(" Tidak ada file PDF di folder input.")
            return
            
        print(f" Mengompres {len(files)} file PDF...")
        for file in files:
            inp = os.path.join(args.input, file)
            out = os.path.join(args.output, f"small_{file}")
            compress_pdf(inp, out, args.power)
    else:
        print(" Path input tidak ditemukan.")

if __name__ == "__main__":
    main()