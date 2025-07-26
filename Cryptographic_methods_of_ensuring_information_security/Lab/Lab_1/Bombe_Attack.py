import string
from itertools import permutations, product

ALPHABET = string.ascii_uppercase

ROTORS = {
    'I':     ('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q'),
    'II':    ('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E'),
    'III':   ('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V'),
}

REFLECTOR = dict(zip(ALPHABET, 'YRUHQSLDPXNGOKMIEBFZCWVJAT'))

def rotate(s):
    return s[1:] + s[0]

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

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
    def __init__(self, rotor_order, rotor_positions):
        self.rotors = []
        for rotor_name, pos in zip(rotor_order, rotor_positions):
            wiring, notch = ROTORS[rotor_name]
            self.rotors.append(Rotor(wiring, notch, pos))

    def reset(self, positions):
        for rotor, pos in zip(self.rotors, positions):
            rotor.position = pos

    def encrypt_letter(self, c):
        if c not in ALPHABET:
            return c

        rotate_next = self.rotors[2].step()
        if rotate_next:
            rotate_next = self.rotors[1].step()
            if rotate_next:
                self.rotors[0].step()

        for rotor in reversed(self.rotors):
            c = rotor.encode_forward(c)

        c = REFLECTOR[c]

        for rotor in self.rotors:
            c = rotor.encode_backward(c)

        return c

    def encrypt_message(self, message):
        message = ''.join(filter(str.isalpha, message)).upper()
        return ''.join(self.encrypt_letter(c) for c in message)

def bombe_attack(ciphertext, crib):
    rotor_combinations = list(permutations(['I', 'II', 'III'], 3))
    positions = list(product(ALPHABET, repeat=3))
    results = []

    print(f"🔍 Đang thử {len(rotor_combinations) * len(positions)} cấu hình...")

    for rotor_order in rotor_combinations:
        for pos in positions:
            machine = Enigma(rotor_order, list(pos))
            machine.reset(list(pos))
            trial = machine.encrypt_message(crib)
            if trial in ciphertext:
                results.append((rotor_order, pos, trial))

    return results

# === Main ===

if __name__ == "__main__":
    ciphertext = read_file("enigma_decryption.txt").strip().upper()
    crib = input("Nhập đoạn crib (plaintext nghi ngờ xuất hiện trong bản mã): ").strip().upper()

    matches = bombe_attack(ciphertext, crib)

    print("\nCác cấu hình phù hợp với crib:")
    if matches:
        for rotor_order, pos, result in matches:
            print(f"  ➤ Rotors: {rotor_order} | Vị trí bắt đầu: {pos} → Mã hóa crib: {result}")
    else:
        print("Không tìm thấy cấu hình phù hợp.")
