import subprocess
import os
import platform

def get_ffmpeg_command(input_file, output_file):
    return [
        'ffmpeg',
        '-i', input_file,
        '-vcodec', 'libx264',
        '-crf', '28',       
        '-preset', 'medium', 
        '-acodec', 'aac',    
        '-y', 
        output_file
    ]

def process_path(target_path):
    target_path = target_path.strip().replace('"', '').replace("'", "")
    
    if os.path.isfile(target_path):
        out = f"compressed_{os.path.basename(target_path)}"
        subprocess.run(get_ffmpeg_command(target_path, out))
        
    elif os.path.isdir(target_path):
        output_folder = os.path.join(target_path, "hasil_kompres")
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            
        exts = ('.mp4', '.mkv', '.mov', '.avi', '.webm')
        files = [f for f in os.listdir(target_path) if f.lower().endswith(exts)]
        
        for f in files:
            inp = os.path.join(target_path, f)
            out = os.path.join(output_folder, f"kecil_{f}")
            print(f"\n>>> Processing: {f}")
            subprocess.run(get_ffmpeg_command(inp, out))
    else:
        print("Path tidak valid!")

if __name__ == "__main__":
    print(f"Sistem Terdeteksi: {platform.system()}")
    path_input = input("Masukkan Path File atau Folder: ")
    process_path(path_input)