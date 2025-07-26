from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

PUBLIC_KEY_FILE = "public_key.pem"
SIGNATURE_FILE = "signature.sig"

def save_signature_to_file(signature):
    try:
        with open(SIGNATURE_FILE, 'wb') as f:
            f.write(signature)
        print("Подпись была сохранена в файл.")
    except Exception as e:
        print(f"Ошибка при сохранении подписи в файл: {e}")

def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    public_key = private_key.public_key()
    with open(PUBLIC_KEY_FILE, "wb") as f:
        f.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )
    print(f"Открытый ключ был сохранен в {PUBLIC_KEY_FILE}")

    message = b"ChuVanDoanN3347"
    signature = private_key.sign(
        message,
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    save_signature_to_file(signature)

def main():
    generate_key_pair()

if __name__ == "__main__":
    main()

