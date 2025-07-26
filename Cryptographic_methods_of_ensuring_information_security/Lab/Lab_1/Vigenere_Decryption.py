def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def repeat_key(key, length):
    key = key.upper()
    return (key * (length // len(key) + 1))[:length]

def vigenere_decrypt(ciphertext, key):
    ciphertext = ''.join(filter(str.isalpha, ciphertext)).upper()
    key = repeat_key(key, len(ciphertext))
    plaintext = ''

    for c, k in zip(ciphertext, key):
        c_val = ord(c) - ord('A')
        k_val = ord(k) - ord('A')
        p_val = (c_val - k_val + 26) % 26
        plaintext += chr(p_val + ord('A'))

    return plaintext

if __name__ == "__main__":
    # Đọc dữ liệu
    ciphertext = read_file('Vigenere_encryption.txt')
    key = read_file('Vigenere_key.txt').strip()

    # Giải mã
    plaintext = vigenere_decrypt(ciphertext, key)

    # Ghi kết quả
    write_file('Vigenere_decryption.txt', plaintext)

    print("Giải mã hoàn tất. Kết quả lưu tại Vigenere_decryption.txt")
