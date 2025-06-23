import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature
from cryptography.fernet import Fernet
import subprocess

PUBLIC_KEY_FILE = "public_key.pem"
SIGNATURE_FILE = "signature.sig"

def load_signature():
    try:
        with open(SIGNATURE_FILE, 'rb') as f:
            signature = f.read()
        return signature
    except FileNotFoundError:
        print(f"Файл подписи не существует: {SIGNATURE_FILE}")
        return None

def load_public_key_from_file(public_key_file):
    try:
        with open(public_key_file, "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )
        return public_key
    except FileNotFoundError:
        print(f"Не найден файл открытого ключа: {public_key_file}")
        return None

def verify_signature(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False

def decrypt_file(filepath, key):
    cipher_suite = Fernet(key)
    with open(filepath, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    
    with open(filepath, 'wb') as file:
        file.write(decrypted_data)

def encrypt_file(filepath, key):
    cipher_suite = Fernet(key)
    with open(filepath, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    
    with open(filepath, 'wb') as file:
        file.write(encrypted_data)

def main():
    signature = load_signature()
    if not signature:
        return

    public_key_file = input("Введите путь к открытому ключу: ").strip()
    public_key = load_public_key_from_file(public_key_file)
    if not public_key:
        return

    message = b"ChuVanDoanN3347"
    
    if verify_signature(public_key, message, signature):
        with open('key.key', 'rb') as key_file:
            key = key_file.read()
        decrypt_file('sys.tat', key)
        subprocess.run(['nano', 'sys.tat'])
        encrypt_file('sys.tat', key)
    else:
        print("Подтверждение не удалось! Невозможно открыть файл sys.tat.")

if __name__ == "__main__":
    main()

