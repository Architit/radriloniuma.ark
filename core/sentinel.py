import time
import socket
import sys
import os

LOG_PATH = "/root/ark/logs/ark_event_journal.log"

def log(msg):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_PATH, "a") as f:
        f.write(f"[{timestamp}] [SENTINEL-0] {msg}\n")
    print(f"[{timestamp}] {msg}")
    sys.stdout.flush()

def check_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1.0)
        return s.connect_ex(('localhost', port)) == 0

if __name__ == "__main__":
    log("Sentinel-0 переведен в режим активного сканирования шлюзов.")
    ports = {8765: "Autopilot", 8766: "MCP_Gateway", 8767: "Mesh_Server"}
    
    while True:
        for port, name in ports.items():
            status = "ONLINE" if check_port(port) else "OFFLINE"
            if status == "OFFLINE":
                log(f"ALERT: Узел {name} (Port {port}) недоступен.")
        time.sleep(300) 
