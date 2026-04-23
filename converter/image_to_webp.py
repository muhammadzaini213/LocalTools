import os
import argparse
from PIL import Image

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", default="input")
    parser.add_argument("-o", "--output", default="output_webp")
    parser.add_argument("--quality", type=int, default=80)
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    files = [f for f in os.listdir(args.input) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

    for file in files:
        img = Image.open(os.path.join(args.input, file))
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGBA")
        else:
            img = img.convert("RGB")
            
        name, _ = os.path.splitext(file)
        img.save(os.path.join(args.output, f"{name}.webp"), "WEBP", quality=args.quality)
        print(f"Converted to WebP: {file}")

if __name__ == "__main__":
    main()