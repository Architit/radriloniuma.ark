import sys

def verify_token(token):
    # Простейшая проверка префикса нашего протокола
    if token.startswith("HEX-"):
        print("[VAVIMA] Доступ разрешен: Узел верифицирован.")
        return True
    print("[VAVIMA] ОТКАЗ: Невалидный токен.")
    return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        verify_token(sys.argv[1])
