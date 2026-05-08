import socket, sys, time

def start_gateway(port, name):
    print(f"[IGNITION] Запуск {name} на порту {port}...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', port))
        s.listen(5)
        while True:
            conn, addr = s.accept()
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) > 2:
        start_gateway(int(sys.argv[1]), sys.argv[2])
