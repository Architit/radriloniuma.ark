import socket
import json

def check_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        return s.connect_ex(('localhost', port)) == 0

def run_diagnostics():
    print("[SCANNER] Запуск активной проверки шлюзов MCP...")
    ports = [8765, 8766, 8767]
    results = {port: "OPEN" if check_port(port) else "CLOSED" for port in ports}
    
    for port, status in results.items():
        print(f"  - Port {port}: {status}")
    
    return results

if __name__ == "__main__":
    run_diagnostics()
