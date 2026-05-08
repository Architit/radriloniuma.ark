import socket
import datetime
import os
import subprocess

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
    log_to_ark("Начало сканирования.")
    ports = {8765: "Autopilot", 8766: "MCP_Gateway", 8767: "Mesh_Server"}
    results = {port: check_port(port) for port in ports}
    
    all_active = True
    print("[SCANNER] Состояние узлов:")
    for port, active in results.items():
        status = "ONLINE" if active else "OFFLINE"
        print(f"  - {ports[port]} (Port {port}): {status}")
        if not active:
            all_active = False
            log_to_ark(f"Критический сбой: {ports[port]} на порту {port} недоступен.")

    if not all_active:
        print("[!] Обнаружены неактивные узлы. Рекомендуется запуск через PM2.")
    
    log_to_ark(f"Диагностика завершена. Все системы в норме: {all_active}")

if __name__ == "__main__":
    run_diagnostics()
