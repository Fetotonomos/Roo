# launch.py
import subprocess
import sys

def run_bots():
    # اجرای همزمان هر دو ربات
    bot1 = subprocess.Popen([sys.executable, "bot1.py"])
    bot2 = subprocess.Popen([sys.executable, "bot2.py"])
    
    # منتظر ماندن برای اتمام هر دو
    bot1.wait()
    bot2.wait()

if __name__ == "__main__":
    run_bots()