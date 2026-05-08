import time
import os

LOG_PATH = "/root/ark/logs/ark_event_journal.log"

def log(msg):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    if os.path.exists(os.path.dirname(LOG_PATH)):
        with open(LOG_PATH, "a") as f:
            f.write(f"[{timestamp}] [SENTINEL] {msg}\n")

if __name__ == "__main__":
    log("Sentinel-0 запущен в автономном режиме.")
    while True:
        # Здесь будет логика проверки портов и авто-рестарта
        time.sleep(60)
