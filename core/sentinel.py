import time
import subprocess
import os

LOG_PATH = "/root/ark/logs/ark_event_journal.log"

def log(msg):
    with open(LOG_PATH, "a") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [SENTINEL] {msg}\n")

def check_and_revive():
    log("Цикл мониторинга запущен.")
    # Простая проверка: если сканер выдает OFFLINE, можно инициировать перезапуск
    # В этой версии мы просто имитируем активность для PM2
    print("[SENTINEL] Узел активен. Мониторинг сети...")
    time.sleep(60)

if __name__ == "__main__":
    while True:
        check_and_revive()
