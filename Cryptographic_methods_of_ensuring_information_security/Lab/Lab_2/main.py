# main.py

from DES import encrypt, decrypt
from secrets import token_bytes

def main():
    message = "Hello from DES Cipher!"
    key = token_bytes(8)

    print("Original message:", message)
    print("Key (hex):", key.hex())

    ciphertext = encrypt(message.encode(), key)
    print("Encrypted (hex):", ciphertext.hex())

    decrypted = decrypt(ciphertext, key)
    print("Decrypted:", decrypted.decode())

if __name__ == "__main__":
    main()
