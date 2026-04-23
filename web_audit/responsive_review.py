import asyncio
import os
from tqdm import tqdm
from playwright.async_api import async_playwright 

async def take_screenshot(context, url, name, width, height, output_dir):
    page = await context.new_page()
    await page.set_viewport_size({"width": width, "height": height})
    
    try:
        await page.goto(url, wait_until="networkidle", timeout=60000)
        
        await page.evaluate("""
            async () => {
                await new Promise((resolve) => {
                    let totalHeight = 0;
                    let distance = 100;
                    let timer = setInterval(() => {
                        let scrollHeight = document.body.scrollHeight;
                        window.scrollBy(0, distance);
                        totalHeight += distance;
                        if(totalHeight >= scrollHeight){
                            clearInterval(timer);
                            resolve();
                        }
                    }, 100);
                });
            }
        """)

        output_path = os.path.join(output_dir, f"{name}.png")
        await page.screenshot(path=output_path, full_page=True)
        return True
    except Exception as e:
        print(f"\n❌ Error {name}: {e}")
        return False
    finally:
        await page.close()

async def main():
    target_url = input("Masukkan URL Web: ")
    is_headless = input("Gunakan Headless? (y/n): ").lower() == 'y'
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(current_dir, "AuditWeb_Zaini")
    os.makedirs(output_dir, exist_ok=True)

    tasks_data = [
        ("Mobile_iPhone", 390, 844),
        ("Tablet_iPad", 820, 1180),
        ("Desktop_FHD", 1920, 1080),
        ("Desktop_4K", 3840, 2160)
    ]

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            executable_path="/usr/bin/brave-browser",
            headless=is_headless
        )
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )

        print(f"\n--- Memulai Audit Playwright (Brave) ---")
        print(f"📁 Output: {output_dir}\n")
        
        tasks = [take_screenshot(context, target_url, name, w, h, output_dir) for name, w, h in tasks_data]
        
        for f in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="Audit Progress", unit="img"):
            await f

        await browser.close()
        print(f"\n✅ Selesai! Semua gambar ada di: {output_dir}")

if __name__ == "__main__":
    asyncio.run(main())