import requests
import time
import os
import sys

def one_shot_monitor():
    print("--- 🎯 ONE-SHOT WEB WATCHER ---")
    target_url = input("🔗 Link yang mau dipantau: ").strip()
    
    if not target_url.startswith(("http://", "https://")):
        target_url = "https://" + target_url

    print(f"\n📡 Siaga... Script akan otomatis berhenti setelah target tercapai.")
    
    # Ambil status awal sebagai patokan
    try:
        initial_response = requests.get(target_url, timeout=10)
        last_content = initial_response.text
        print("✅ Status awal tercatat. Menunggu perubahan...")
    except:
        last_content = None
        print("💀 Status awal: Server DOWN. Menunggu sampai UP...")

    while True:
        try:
            response = requests.get(target_url, timeout=10)
            
            # KONDISI 1: Tadi mati, sekarang hidup
            if last_content is None:
                print(f"\n✨ [{time.strftime('%H:%M:%S')}] SERVER SUDAH BANGUN!")
                break # KELUAR DARI LOOP
            
            # KONDISI 2: Konten berubah (Update Nilai/Pengumuman)
            if response.text != last_content:
                print(f"\n🔔 [{time.strftime('%H:%M:%S')}] ADA UPDATE DI WEB!")
                break # KELUAR DARI LOOP
            
            print(f"💤 [{time.strftime('%H:%M:%S')}] Masih sama...", end='\r')
            
        except requests.exceptions.RequestException:
            # Jika sedang menunggu server yang down
            print(f"💀 [{time.strftime('%H:%M:%S')}] Server masih down...", end='\r')

        time.sleep(30) # Cek tiap 30 detik biar nggak nyiksa server

    # --- ACTION SETELAH BERHASIL ---
    print("\n\n" + "!"*30)
    print("🎉 TARGET TERCAPAI! BERHENTI.")
    print("!"*30)
    
    # Suara beep berkali-kali biar kedengeran
    for _ in range(5):
        print('\a', end='', flush=True)
        time.sleep(0.3)
    
    # Notifikasi visual
    os.system(f'notify-send "TARGET TERCAPAI!" "Web {target_url} sudah berubah/aktif!"')
    
    # Script selesai (Self-Terminate)
    sys.exit()

if __name__ == "__main__":
    one_shot_monitor()