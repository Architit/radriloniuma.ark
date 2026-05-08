import time, json, os, sys, socket
from radriloniuma.ark.protocols.vavima.gate import verify_token

LOG_PATH = "/root/ark/logs/ark_event_journal.log"
TOKEN_PATH = "/tmp/ark_session_token"

def log(msg):
    ts = time.strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_PATH, "a") as f: f.write(f"[{ts}] [SENTINEL-0] {msg}\n")
    print(f"[{ts}] {msg}"); sys.stdout.flush()

def heartbeat(token):
    if not verify_token(token): return
    ports = {8765: "Autopilot", 8766: "MCP_Gateway", 8767: "Mesh_Server"}
    for p, name in ports.items():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0)
            status = "HEALTHY" if s.connect_ex(('localhost', p)) == 0 else "DEAD"
            log(f"Heartbeat {name} ({p}): {status}")

if __name__ == "__main__":
    log("Sentinel-0: Режим Heartbeat активирован.")
    while True:
        if os.path.exists(TOKEN_PATH):
            with open(TOKEN_PATH, "r") as f: heartbeat(f.read().strip())
        time.sleep(300)
