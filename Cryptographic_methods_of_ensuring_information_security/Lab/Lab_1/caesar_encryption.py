def caesar_encrypt(text, key):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def encrypt_file(input_filename, output_filename, key):
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            plaintext = infile.read()
        
        ciphertext = caesar_encrypt(plaintext, key)

        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(ciphertext)

        print(f"Đã mã hóa xong. Kết quả lưu trong '{output_filename}'.")

    except FileNotFoundError:
        print(f"Không tìm thấy file '{input_filename}'.")
    except Exception as e:
        print(f"Lỗi: {e}")

# ===============================
# Chương trình chính
# ===============================
if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "caesar_encryption.txt"

    try:
        key = int(input("Nhập khóa Caesar (số nguyên): "))
        encrypt_file(input_file, output_file, key)
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")
