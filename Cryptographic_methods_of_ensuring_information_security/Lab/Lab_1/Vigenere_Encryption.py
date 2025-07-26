def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def repeat_key(key, length):
    key = key.upper()
    return (key * (length // len(key) + 1))[:length]

def vigenere_encrypt(plaintext, key):
    plaintext = ''.join(filter(str.isalpha, plaintext)).upper()
    key = repeat_key(key, len(plaintext))
    ciphertext = ''

    for p, k in zip(plaintext, key):
        p_val = ord(p) - ord('A')
        k_val = ord(k) - ord('A')
        c_val = (p_val + k_val) % 26
        ciphertext += chr(c_val + ord('A'))

    return ciphertext

if __name__ == "__main__":
    # Đọc dữ liệu
    plaintext = read_file('input.txt')
    key = read_file('Vigenere_key.txt').strip()

    # Mã hóa
    ciphertext = vigenere_encrypt(plaintext, key)

    # Ghi kết quả
    write_file('Vigenere_encryption.txt', ciphertext)

    print("Mã hóa hoàn tất. Kết quả lưu tại Vigenere_encryption.txt")
