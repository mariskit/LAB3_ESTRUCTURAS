import concurrent.futures
from Crypto.Hash import SHA3_512
import threading

# Variables
found = threading.Event()  # para detener todos los hilos cuando se encuentre la contraseña
user = 'danielhoyos'
salt = "90646ae569c6626897d9db1eae2d6e7a"
pwd = '4012ba22f52f54896679d5b3421f3446daead21d64432ac17bfdc525eb72d6880e8351de243b773c23446da07b7372099236c112125a17f827b9aaa045359b15'
salt_b = bytes.fromhex(salt)
rockyou_path = 'rockyou.txt'
chunk_size = 1000  # Tamaño de los bloques

def hash_password(password, pepper):
    H = SHA3_512.new()
    password_b = bytes(password, 'utf-8')
    H.update(password_b)
    
    pepper_b = pepper.to_bytes(1, 'big')
    H.update(pepper_b)
    
    H.update(salt_b)
    
    return H.hexdigest()

def worker_task(passwords):
    #Esclavo
    for password in passwords:
        if found.is_set():
            return None
        for pepper in range(256):
            pwd_h = hash_password(password, pepper)
            if pwd == pwd_h:
                found.set()
                print(f"Contraseña encontrada: {password}")
                return password
    return None

def main():
    #Función principal que actúa como el master
    num_threads = 6  # Ajusta estar según el número de núcleos de la CPU
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        with open(rockyou_path, 'r', encoding='latin-1') as file:
            while not found.is_set():

                chunk = [line.strip() for line in file.readlines(chunk_size)]
                if not chunk:
                    break
                futures.append(executor.submit(worker_task, chunk))

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                print(f"Password found: {result}")
                break

if __name__ == "__main__":
    main()
