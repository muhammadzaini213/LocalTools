import os
from pydub import AudioSegment
from tqdm import tqdm

def batch_wav():
    input_folder = "input_audio"
    output_folder = "output_wav"
    
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
        print(f"📁 Folder '{input_folder}' dibuat. Taruh MP3 di sana!")
        return
    
    os.makedirs(output_folder, exist_ok=True)
    files = [f for f in os.listdir(input_folder) if f.lower().endswith(".mp3")]

    if not files:
        print("❌ Tidak ada file MP3.")
        return

    print(f"🔊 Mengonversi {len(files)} file ke WAV...")
    for filename in tqdm(files, desc="Progress WAV", unit="file"):
        try:
            path_in = os.path.join(input_folder, filename)
            path_out = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.wav")
            
            audio = AudioSegment.from_mp3(path_in)
            audio.export(path_out, format="wav")
        except Exception as e:
            print(f" Error {filename}: {e}")

if __name__ == "__main__":
    batch_wav()