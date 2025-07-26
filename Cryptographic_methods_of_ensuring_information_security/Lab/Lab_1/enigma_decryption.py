import string

ALPHABET = string.ascii_uppercase

# Rotor wiring mẫu (Enigma I)
ROTORS = {
    'I':     ('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q'),
    'II':    ('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E'),
    'III':   ('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V'),
}

# Reflector mẫu (UKW-B)
REFLECTOR = dict(zip(ALPHABET, 'YRUHQSLDPXNGOKMIEBFZCWVJAT'))

def rotate(s):
    return s[1:] + s[0]

class Plugboard:
    def __init__(self, wiring_pairs=None):
        self.wiring = dict(zip(ALPHABET, ALPHABET))  # Mặc định không hoán vị
        if wiring_pairs:
            for a, b in wiring_pairs:
                self.wiring[a] = b
                self.wiring[b] = a

    def swap(self, c):
        return self.wiring.get(c, c)

class Rotor:
    def __init__(self, wiring, notch, position='A'):
        self.wiring = wiring
        self.notch = notch
        self.position = position

    def encode_forward(self, c):
        idx = (ALPHABET.index(c) + ALPHABET.index(self.position)) % 26
        return self.wiring[idx]

    def encode_backward(self, c):
        idx = (self.wiring.index(c) - ALPHABET.index(self.position)) % 26
        return ALPHABET[idx]

    def step(self):
        self.position = rotate(self.position)[0]
        return self.position == self.notch

class Enigma:
    def __init__(self, rotor_order, rotor_positions, plugboard_pairs=None):
        self.plugboard = Plugboard(plugboard_pairs)
        self.rotors = []
        for rotor_name, pos in zip(rotor_order, rotor_positions):
            wiring, notch = ROTORS[rotor_name]
            self.rotors.append(Rotor(wiring, notch, pos))

    def encrypt_letter(self, c):
        if c not in ALPHABET:
            return c

        # Bước rotor
        rotate_next = self.rotors[2].step()
        if rotate_next:
            rotate_next = self.rotors[1].step()
            if rotate_next:
                self.rotors[0].step()

        # Qua plugboard lần 1
        c = self.plugboard.swap(c)

        # Qua rotor forward
        for rotor in reversed(self.rotors):
            c = rotor.encode_forward(c)

        # Reflector
        c = REFLECTOR[c]

        # Qua rotor backward
        for rotor in self.rotors:
            c = rotor.encode_backward(c)

        # Qua plugboard lần 2
        c = self.plugboard.swap(c)

        return c

    def encrypt_message(self, message):
        message = ''.join(filter(str.isalpha, message)).upper()
        return ''.join(self.encrypt_letter(c) for c in message)

# ==== File Helpers ====

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# ==== Main ====

if __name__ == "__main__":
    # === Cấu hình giống khi mã hóa ===
    rotor_order = ['I', 'II', 'III']
    rotor_positions = ['A', 'A', 'A']  # Phải khớp với lúc mã hóa

    plugboard_pairs = [
        ('A', 'M'),
        ('T', 'G'),
        ('L', 'P'),
        ('O', 'K'),
        ('E', 'R')
    ]

    # Đọc ciphertext từ file mã hóa
    ciphertext = read_file('enigma_encryption.txt')

    # Khởi tạo lại máy Enigma với cấu hình cũ
    enigma = Enigma(rotor_order, rotor_positions, plugboard_pairs)

    # Giải mã (thực chất gọi encrypt_message lại lần nữa)
    plaintext = enigma.encrypt_message(ciphertext)

    # Ghi ra file
    write_file('enigma_decryption.txt', plaintext)

    print("Giải mã hoàn tất. Kết quả lưu tại enigma_decryption.txt")
