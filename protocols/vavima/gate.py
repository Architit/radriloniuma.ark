import hashlib

def verify_access(key):
    # Простейшая реализация гексагонального ключа
    check = hashlib.sha256(key.encode()).hexdigest()
    return check.startswith("000") # Условный уровень сложности

if __name__ == "__main__":
    print("[VAVIMA] Gate active. Waiting for key...")
