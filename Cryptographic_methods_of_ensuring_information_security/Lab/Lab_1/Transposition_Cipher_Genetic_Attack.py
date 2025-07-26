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

# Hàm fitness: đếm số từ tiếng Anh phổ biến xuất hiện
def fitness(text, common_words):
    words = text.lower().split()
    return sum(1 for word in words if word in common_words)

# Đột biến một hoán vị
def mutate(key):
    new_key = key[:]
    a, b = random.sample(range(len(key)), 2)
    new_key[a], new_key[b] = new_key[b], new_key[a]
    return new_key

# Chọn cá thể tốt nhất từ quần thể
def select(population, fitnesses, num):
    sorted_pop = sorted(zip(population, fitnesses), key=lambda x: x[1], reverse=True)
    return [x[0] for x in sorted_pop[:num]]

# Tạo quần thể ban đầu
def initial_population(size, key_len):
    base = list(range(1, key_len + 1))
    return [random.sample(base, len(base)) for _ in range(size)]

# Thuật toán di truyền
def genetic_attack(ciphertext, common_words, key_len=6, generations=1000, pop_size=100):
    population = initial_population(pop_size, key_len)
    best_plaintext = ""
    best_score = -1

    for gen in range(generations):
        fitnesses = [fitness(columnar_decrypt(ciphertext, k), common_words) for k in population]
        best_gen_score = max(fitnesses)
        if best_gen_score > best_score:
            best_score = best_gen_score
            best_plaintext = columnar_decrypt(ciphertext, population[fitnesses.index(best_gen_score)])
        selected = select(population, fitnesses, pop_size // 2)
        next_gen = selected[:]
        while len(next_gen) < pop_size:
            parent = random.choice(selected)
            child = mutate(parent)
            next_gen.append(child)
        population = next_gen

    return best_plaintext

# ========================
# Chạy chương trình chính
# ========================
if __name__ == "__main__":
    ciphertext = load_ciphertext("Columnar_Transposition_Cipher_encryption.txt")

    # Tập từ tiếng Anh đơn giản
    common_words = {
        "the", "be", "to", "of", "and", "a", "in", "that", "have", "i",
        "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
        "this", "but", "his", "by", "from", "they", "we", "say", "her",
        "she", "or", "an", "will", "my", "one", "all", "would", "there",
        "their", "what", "so", "up", "out", "if", "about", "who", "get",
        "which", "go", "me"
    }

    result = genetic_attack(ciphertext, common_words, key_len=6, generations=1000, pop_size=100)

    with open("Transposition_Genetic_Analysis_Result.txt", "w", encoding="utf-8") as f:
        f.write(result)

    print("Phân tích di truyền hoàn tất. Kết quả lưu trong 'Transposition_Genetic_Analysis_Result.txt'")
