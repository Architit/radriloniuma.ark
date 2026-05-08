import socket
import datetime
import os

LOG_PATH = "/root/ark/logs/ark_event_journal.log"

def log_to_ark(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "a") as f:
            f.write(f"[{timestamp}] [SCANNER_AGENT] {message}\n")

def check_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        return s.connect_ex(('localhost', port)) == 0

def run_diagnostics():
    log_to_ark("Начало диагностики портов.")
    ports = [8765, 8766, 8767]
    results = {port: "OPEN" if check_port(port) else "CLOSED" for port in ports}
    
    print("[SCANNER] Результаты проверки:")
    for port, status in results.items():
        print(f"  - Port {port}: {status}")
    
    log_to_ark(f"Диагностика завершена. Статус портов: {results}")

if __name__ == "__main__":
    run_diagnostics()
