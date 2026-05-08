import hashlib
import time

def generate_token():
    # Генерируем ключ на основе времени и соли
    seed = f"ARK-{time.time()}-VAVIMA"
    token = hashlib.sha256(seed.encode()).hexdigest()
    return f"HEX-{token[:16]}"

if __name__ == "__main__":
    print(generate_token())
