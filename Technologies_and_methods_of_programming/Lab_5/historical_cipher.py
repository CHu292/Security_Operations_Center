import tkinter as tk
from tkinter import filedialog
import numpy as np

# Mã hóa ma trận (Matrix Encryption) hỗ trợ Unicode
def matrix_encrypt(text, key_matrix):
    text_vector = [ord(char) for char in text]
    while len(text_vector) % len(key_matrix) != 0:
        text_vector.append(0)

    text_matrix = np.array(text_vector).reshape(-1, len(key_matrix)).T
    encrypted_matrix = np.dot(key_matrix, text_matrix) % 1114112
    encrypted_text = ''.join(chr(num) for num in encrypted_matrix.T.flatten())
    return encrypted_text

def matrix_decrypt(text, key_matrix):
    text_vector = [ord(char) for char in text]
    text_matrix = np.array(text_vector).reshape(-1, len(key_matrix)).T

    # Kiểm tra khả nghịch của ma trận
    det = int(round(np.linalg.det(key_matrix)))
    if det == 0:
        return "Error: Key matrix is not invertible!"

    # Tính ma trận nghịch đảo modulo
    det_mod_inverse = pow(det, -1, 1114112)
    adjugate_matrix = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 1114112
    inverse_matrix = (det_mod_inverse * adjugate_matrix) % 1114112

    decrypted_matrix = np.dot(inverse_matrix, text_matrix) % 1114112
    decrypted_text = ''.join(chr(num) for num in decrypted_matrix.T.flatten() if num > 0)
    return decrypted_text

# Mã hóa bằng từ khóa (Keyword Cipher) hỗ trợ Unicode
def keyword_encrypt(text, keyword):
    all_chars = ''.join(chr(i) for i in range(1114112))
    keyword_unique = ''.join(sorted(set(keyword), key=keyword.index))
    cipher_chars = keyword_unique + ''.join(c for c in all_chars if c not in keyword_unique)

    cipher_map = {all_chars[i]: cipher_chars[i] for i in range(len(all_chars))}
    try:
        encrypted_text = ''.join(cipher_map[char] for char in text)
    except KeyError:
        return "Error: Invalid character in input text!"
    return encrypted_text

def keyword_decrypt(text, keyword):
    all_chars = ''.join(chr(i) for i in range(1114112))
    keyword_unique = ''.join(sorted(set(keyword), key=keyword.index))
    cipher_chars = keyword_unique + ''.join(c for c in all_chars if c not in keyword_unique)

    reverse_cipher_map = {cipher_chars[i]: all_chars[i] for i in range(len(all_chars))}
    try:
        decrypted_text = ''.join(reverse_cipher_map[char] for char in text)
    except KeyError:
        return "Error: Invalid character in input text!"
    return decrypted_text

# Giao diện
def encrypt():
    text = input_text.get("1.0", "end-1c")
    mode = mode_var.get()
    if mode == "Matrix":
        key = np.array([[2, 3], [1, 4]])
        result = matrix_encrypt(text, key)
    elif mode == "Keyword":
        keyword = shift_entry.get()
        if not keyword:
            result = "Error: Keyword cannot be empty!"
        else:
            result = keyword_encrypt(text, keyword)
    else:
        result = "Invalid mode!"
    output_text.delete("1.0", "end")
    output_text.insert("1.0", result)

def decrypt():
    text = input_text.get("1.0", "end-1c")
    mode = mode_var.get()
    if mode == "Matrix":
        key = np.array([[2, 3], [1, 4]])
        result = matrix_decrypt(text, key)
    elif mode == "Keyword":
        keyword = shift_entry.get()
        if not keyword:
            result = "Error: Keyword cannot be empty!"
        else:
            result = keyword_decrypt(text, keyword)
    else:
        result = "Invalid mode!"
    output_text.delete("1.0", "end")
    output_text.insert("1.0", result)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            input_text.delete("1.0", "end")
            input_text.insert("1.0", file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(output_text.get("1.0", "end-1c"))

# Cấu hình giao diện
window = tk.Tk()
window.title("Matrix and Keyword Cipher")

tk.Label(window, text="Input Text:").pack()
input_text = tk.Text(window, height=5, width=50)
input_text.pack()

tk.Label(window, text="Mode (Matrix/Keyword):").pack()
mode_var = tk.StringVar(value="Matrix")
mode_menu = tk.OptionMenu(window, mode_var, "Matrix", "Keyword")
mode_menu.pack()

tk.Label(window, text="Keyword/Matrix Key:").pack()
shift_entry = tk.Entry(window)
shift_entry.pack()

tk.Button(window, text="Encrypt", command=encrypt).pack()
tk.Button(window, text="Decrypt", command=decrypt).pack()
tk.Button(window, text="Open File", command=open_file).pack()
tk.Button(window, text="Save File", command=save_file).pack()

tk.Label(window, text="Output Text:").pack()
output_text = tk.Text(window, height=5, width=50)
output_text.pack()

window.mainloop()
