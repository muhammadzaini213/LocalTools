import yt_dlp
import os

def download_fb_reels(url):
    # Folder penyimpanan hasil
    output_folder = "downloaded_reels"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    ydl_opts = {
        # 'best' akan mengambil kualitas tertinggi yang tersedia
        'format': 'bestvideo+bestaudio/best',
        # Lokasi penyimpanan dan format nama file (Judul Video.mp4)
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
        # Menambahkan User-Agent agar tidak dianggap bot/spam oleh FB
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        # Log status download
        'quiet': False,
        'no_warnings': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Sedang mengambil informasi video...")
            ydl.download([url])
            print(f"\nSelesai! Cek folder '{output_folder}'")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    link = input("Masukkan Link Facebook Reels: ").strip()
    if "facebook.com" in link:
        download_fb_reels(link)
    else:
        print("Link sepertinya bukan dari Facebook.")