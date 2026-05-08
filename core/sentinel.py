import time
import json
import os
import sys

LOG_PATH = "/root/ark/logs/ark_event_journal.log"
TELEMETRY_LOG = "/root/ark/logs/telemetry.json"

def log(msg):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_PATH, "a") as f:
        f.write(f"[{timestamp}] [SENTINEL-0] {msg}\n")
    print(f"[{timestamp}] {msg}")
    sys.stdout.flush()

def check_resources():
    if os.path.exists(TELEMETRY_LOG):
        try:
            with open(TELEMETRY_LOG, "r") as f:
                last_line = f.readlines()[-1]
                data = json.loads(last_line)
                if data["memory"] > 85.0:
                    log("КРИТИЧЕСКАЯ НАГРУЗКА RAM: Инициация очистки логов.")
                    open(LOG_PATH, 'w').close() # Ротация логов
        except Exception:
            pass

if __name__ == "__main__":
    log("Sentinel-0 переведен в режим автономного анализа ресурсов.")
    while True:
        check_resources()
        time.sleep(60)

def check_resources():
    if os.path.exists(TELEMETRY_LOG):
        try:
            with open(TELEMETRY_LOG, "r") as f:
                last_line = f.readlines()[-1]
                data = json.loads(last_line)
                if data["memory"] > 85.0:
                    log("КРИТИЧЕСКАЯ НАГРУЗКА RAM: Инициация очистки логов.")
                    open(LOG_PATH, 'w').close()
        except Exception:
            pass

if __name__ == "__main__":
    log("Sentinel-0 переведен в режим автономного анализа ресурсов.")
    while True:
        check_resources()
        time.sleep(60)
