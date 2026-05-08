import time, json, os, sys, socket, subprocess

LOG_PATH = "/root/ark/logs/ark_event_journal.log"
TOKEN_PATH = "/tmp/ark_session_token"
ORCHESTRATOR_PATH = "/root/ark/orchestrator.sh"

def log(msg):
    ts = time.strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_PATH, "a") as f: f.write(f"[{ts}] [SENTINEL-0] {msg}\n")
    print(f"[{ts}] {msg}"); sys.stdout.flush()

def heartbeat(token):
    if not token.startswith("HEX-"): return
    ports = {8765: "Autopilot", 8766: "MCP_Gateway", 8767: "Mesh_Server"}
    for p, name in ports.items():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0)
            if s.connect_ex(('localhost', p)) != 0:
                log(f"ALERT: {name} DEAD. Восстановление...")
                # Вызываем оркестратор напрямую по полному пути
                subprocess.run([ORCHESTRATOR_PATH, "ignite"], capture_output=True)
            else:
                log(f"Heartbeat {name}: HEALTHY")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        heartbeat(sys.argv[1])
    else:
        log("Sentinel-0: Autonomous Recovery Mode.")
        while True:
            if os.path.exists(TOKEN_PATH):
                with open(TOKEN_PATH, "r") as f: heartbeat(f.read().strip())
            time.sleep(300)
