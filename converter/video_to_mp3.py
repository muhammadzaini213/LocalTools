import os
from moviepy.editor import VideoFileClip

def convert_to_mp3():
    print("--- 🎵 LOCAL VIDEO TO MP3 CONVERTER ---")
    
    video_path = input("📂 Masukkan lokasi/nama file video: ").strip()
    
    if not os.path.exists(video_path):
        print("❌ File tidak ditemukan! Pastikan path-nya benar.")
        return

    try:
        base_name = os.path.splitext(video_path)[0]
        output_path = f"{base_name}.mp3"

        print(f"⏳ Sedang mengekstrak audio dari: {video_path}...")
        
        video = VideoFileClip(video_path)
        video.audio.write_audiofile(output_path)
        
        video.close()

        print(f"\n✅ BERHASIL! File audio tersimpan sebagai: {output_path}")
        
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    convert_to_mp3()