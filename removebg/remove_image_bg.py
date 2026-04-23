import os
import io
import argparse
from PIL import Image
from rembg import remove, new_session

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", default="input")
    parser.add_argument("-o", "--output", default="output_nobg")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    session = new_session()

    files = [f for f in os.listdir(args.input) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    
    for file in files:
        input_path = os.path.join(args.input, file)
        with open(input_path, "rb") as f:
            data = f.read()
        
        output_data = remove(data, session=session)
        img = Image.open(io.BytesIO(output_data)).convert("RGBA")
        
        name, _ = os.path.splitext(file)
        img.save(os.path.join(args.output, f"{name}.png"))
        print(f"Removed BG: {file}")

if __name__ == "__main__":
    main()