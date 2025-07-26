def caesar_decrypt(text, key):
    decrypted = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char
    return decrypted

def brute_force_attack(input_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            ciphertext = infile.read()

        print("Kết quả brute-force Caesar Cipher:\n")
        for key in range(1, 26):
            decrypted = caesar_decrypt(ciphertext, key)
            print(f"[Key {key:2}] {decrypted}")
    
    except FileNotFoundError:
        print(f"Không tìm thấy file '{input_filename}'.")
    except Exception as e:
        print(f"Lỗi: {e}")

# ===============================
# Chương trình chính
# ===============================
if __name__ == "__main__":
    input_file = "caesar_encryption.txt"
    brute_force_attack(input_file)
