def caesar_decrypt(ciphertext, key):
    result = ""

    for char in ciphertext:
        if char.isalpha():
            # Giữ nguyên chữ hoa/chữ thường
            offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - offset - key) % 26 + offset)
            result += decrypted_char
        else:
            # Không thay đổi ký tự không phải chữ cái
            result += char

    return result

def brute_force_caesar(ciphertext):
    print("\n[+] Thử tất cả các khóa (1 đến 25):\n")
    for key in range(1, 26):
        decrypted = caesar_decrypt(ciphertext, key)
        print(f"Key {key:2d}: {decrypted}")

if __name__ == "__main__":
    ciphertext = input("Nhập ciphertext cần giải mã: ")
    brute_force_caesar(ciphertext)
