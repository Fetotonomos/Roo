import asyncio
import subprocess
import sys

async def run_bot(script_name):
    """اجرای یک ربات و نمایش خروجی آن"""
    process = await asyncio.create_subprocess_exec(
        sys.executable, script_name,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    
    # نمایش خروجی‌ها به صورت همزمان
    while True:
        line = await process.stdout.readline()
        if not line:
            break
        print(f"[{script_name}] {line.decode().strip()}")
    
    return await process.wait()

async def main():
    # اجرای همزمان هر دو ربات
    tasks = [
        run_bot("bot1.py"),
        run_bot("bot2.py")
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("🛑 ربات‌ها متوقف شدند.")