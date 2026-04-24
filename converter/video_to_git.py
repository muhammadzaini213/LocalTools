import os
from moviepy.editor import VideoFileClip
from tqdm import tqdm

def convert_video_to_gif():
    input_folder = "input_videos"
    output_folder = "output_gifs"
    
    # Setup folders
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
        print(f"📁 Folder '{input_folder}' dibuat. Taruh video kamu di sana!")
        return
    os.makedirs(output_folder, exist_ok=True)

    # List file video
    valid_extensions = (".mp4", ".mkv", ".avi", ".mov", ".flv")
    files = [f for f in os.listdir(input_folder) if f.lower().endswith(valid_extensions)]

    if not files:
        print(f"❌ Tidak ada file video di folder '{input_folder}'.")
        return

    print(f"🎬 Ditemukan {len(files)} video. Memulai proses konversi...")

    for filename in tqdm(files, desc="Converting", unit="file"):
        try:
            video_path = os.path.join(input_folder, filename)
            file_base = os.path.splitext(filename)[0]
            output_path = os.path.join(output_folder, f"{file_base}.gif")

            # Load video
            clip = VideoFileClip(video_path)
            
            # --- OPTIMASI GIF (Agar ukuran tidak raksasa) ---
            # 1. Resize: Ubah lebar ke 480px (tinggi menyesuaikan)
            # 2. FPS: Turunkan ke 10 atau 12 (standar GIF yang efisien)
            optimized_clip = clip.resize(width=480).set_fps(10)
            
            # Export
            # program='ffmpeg' memastikan proses lebih cepat di Linux
            optimized_clip.write_gif(output_path, program='ffmpeg', logger=None)
            
            # Tutup clip untuk membebaskan RAM
            clip.close()
            
        except Exception as e:
            print(f"\n❌ Gagal memproses {filename}: {e}")

    print(f"\n✅ Selesai! GIF kamu ada di folder: {output_folder}")

if __name__ == "__main__":
    convert_video_to_gif()