import string
import random
from collections import Counter

# ====== Bigram frequency (log-approximation) ======
ENGLISH_BIGRAM_FREQ = {
    'TH': 2.71, 'HE': 2.33, 'IN': 2.03, 'ER': 1.78, 'AN': 1.61,
    'RE': 1.41, 'ON': 1.32, 'AT': 1.21, 'EN': 1.13, 'ND': 1.07,
    'TI': 0.99, 'ES': 0.95, 'OR': 0.94, 'TE': 0.93, 'OF': 0.92,
    'ED': 0.90, 'IS': 0.89, 'IT': 0.88, 'AL': 0.88, 'AR': 0.87
}
DEFAULT_SCORE = -1.5
ENGLISH_FREQ_ORDER = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

# ====== Utility functions ======

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def clean_text(text):
    return ''.join([c.upper() for c in text if c.isalpha()])

def frequency_analysis(ciphertext):
    counter = Counter(ciphertext)
    sorted_letters = [pair[0] for pair in counter.most_common()]
    return sorted_letters

def create_freq_key(cipher_freq_order):
    return dict(zip(cipher_freq_order, ENGLISH_FREQ_ORDER))

def decrypt(ciphertext, key_map):
    result = ''
    for char in ciphertext.upper():
        if char in key_map:
            result += key_map[char]
        else:
            result += char
    return result

def bigram_score(text):
    score = 0.0
    for i in range(len(text) - 1):
        pair = text[i:i+2]
        if not pair.isalpha():
            continue
        score += ENGLISH_BIGRAM_FREQ.get(pair, DEFAULT_SCORE)
    return score

def complete_key(partial_key):
    full_key = {}
    used = set(partial_key.values())
    remaining = [c for c in ENGLISH_FREQ_ORDER if c not in used]
    i = 0
    for c in string.ascii_uppercase:
        if c in partial_key:
            full_key[c] = partial_key[c]
        else:
            full_key[c] = remaining[i]
            i += 1
    return full_key

def swap_key(key):
    k = key.copy()
    a, b = random.sample(string.ascii_uppercase, 2)
    k[a], k[b] = k[b], k[a]
    return k

def hill_climb(ciphertext, initial_key, max_iter=5000):
    best_key = initial_key.copy()
    best_plain = decrypt(ciphertext, best_key)
    best_score = bigram_score(best_plain)

    for _ in range(max_iter):
        new_key = swap_key(best_key)
        new_plain = decrypt(ciphertext, new_key)
        new_score = bigram_score(new_plain)

        if new_score > best_score:
            best_key = new_key
            best_score = new_score
            best_plain = new_plain
    return best_plain, best_key, best_score

def shuffle_key(key):
    shuffled = list(key.values())
    random.shuffle(shuffled)
    return dict(zip(string.ascii_uppercase, shuffled))

# ====== Multi-run hill climbing ======

def multi_hill_climb(ciphertext, base_key, runs=30, max_iter=5000):
    best_overall_score = float('-inf')
    best_overall_plain = ''
    best_overall_key = {}

    for i in range(runs):
        # Khởi tạo key khác nhau mỗi lần
        if i == 0:
            current_key = base_key.copy()  # từ phân tích tần suất
        else:
            current_key = shuffle_key(base_key)

        plain, key, score = hill_climb(ciphertext, current_key, max_iter)

        if score > best_overall_score:
            best_overall_score = score
            best_overall_plain = plain
            best_overall_key = key

    return best_overall_plain, best_overall_key

# ====== Main program ======

if __name__ == "__main__":
    print("🔍 Đang đọc ciphertext và phân tích...")
    ciphertext = read_file("Substitution_Cipher_encryption.txt")
    cleaned = clean_text(ciphertext)

    # Phân tích tần suất và tạo key ban đầu
    freq_order = frequency_analysis(cleaned)
    freq_key = create_freq_key(freq_order)
    initial_key = complete_key(freq_key)

    # Chạy nhiều lần hill climbing để tối ưu
    print("Đang chạy nhiều vòng Hill Climbing để tối ưu...")
    plaintext, final_key = multi_hill_climb(ciphertext, initial_key, runs=30, max_iter=5000)

    # Ghi kết quả ra file
    write_file("Demo_Substitution_Cipher_decryption.txt", plaintext)

    key_output = '\n'.join([f"{k} -> {v}" for k, v in sorted(final_key.items())])
    write_file("Demo_Substitution_Cipher_key.txt", key_output)

    print("Hoàn tất! Bản giải tốt nhất đã được ghi:")
    print("- Substitution_Cipher_decryption.txt")
    print("- Substitution_Cipher_key.txt")
