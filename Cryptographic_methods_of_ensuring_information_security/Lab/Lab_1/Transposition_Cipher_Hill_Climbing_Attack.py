import math
import random

# Đọc bản mã từ file
def load_ciphertext(filename="Columnar_Transposition_Cipher_encryption.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().replace("\n", "").strip()

# Giải mã theo hoán vị (key)
def columnar_decrypt(ciphertext, key):
    num_cols = len(key)
    num_rows = math.ceil(len(ciphertext) / num_cols)
    total_cells = num_cols * num_rows
    padding = total_cells - len(ciphertext)

    col_lengths = [num_rows] * num_cols
    for i in range(padding):
        col_idx = key.index(num_cols - i)
        col_lengths[col_idx] -= 1

    cols = [''] * num_cols
    index = 0
    sorted_key = sorted(range(num_cols), key=lambda x: key[x])
    for col_pos in sorted_key:
        length = col_lengths[col_pos]
        cols[col_pos] = ciphertext[index:index + length]
        index += length

    plaintext = ''
    for row in range(num_rows):
        for col in range(num_cols):
            if row < len(cols[col]):
                plaintext += cols[col][row]

    return plaintext

# Hàm đánh giá bản rõ dựa trên từ điển đơn giản
def fitness(text, common_words):
    words = text.lower().split()
    return sum(1 for word in words if word in common_words)

# Hill Climbing Attack
def hill_climb(ciphertext, common_words, key_len=6, max_iterations=5000):
    current_key = random.sample(range(1, key_len + 1), key_len)
    current_plaintext = columnar_decrypt(ciphertext, current_key)
    current_score = fitness(current_plaintext, common_words)

    for _ in range(max_iterations):
        new_key = current_key[:]
        a, b = random.sample(range(key_len), 2)
        new_key[a], new_key[b] = new_key[b], new_key[a]
        new_plaintext = columnar_decrypt(ciphertext, new_key)
        new_score = fitness(new_plaintext, common_words)

        if new_score > current_score:
            current_key = new_key
            current_score = new_score
            current_plaintext = new_plaintext

    return current_plaintext, current_key, current_score

# ========================
# Chạy chương trình chính
# ========================
if __name__ == "__main__":
    ciphertext = load_ciphertext("Columnar_Transposition_Cipher_encryption.txt")

    # Bộ từ tiếng Anh đơn giản
    common_words = {
        "the", "be", "to", "of", "and", "a", "in", "that", "have", "i",
        "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
        "this", "but", "his", "by", "from", "they", "we", "say", "her",
        "she", "or", "an", "will", "my", "one", "all", "would", "there",
        "their", "what", "so", "up", "out", "if", "about", "who", "get",
        "which", "go", "me"
    }

    result_text, final_key, score = hill_climb(ciphertext, common_words, key_len=6, max_iterations=5000)

    with open("Transposition_Hill_Climbing_Result.txt", "w", encoding="utf-8") as f:
        f.write(f"Key used: {final_key}\nScore: {score}\nDecrypted Text:\n{result_text}")

    print("Hill Climbing hoàn tất. Kết quả lưu tại 'Transposition_Hill_Climbing_Result.txt'")
