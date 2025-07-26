#!/usr/bin/env python3
import random
import time
from math import gcd

# -----------------------------------------------------------------------------
# 1. Prime Test: Miller–Rabin
# -----------------------------------------------------------------------------
def is_prime(n, k=5):
    if n < 2: return False
    for p in [2,3,5,7,11,13,17,19,23]:
        if n % p == 0:
            return n == p
    # write n-1 = 2^r * d
    r, d = 0, n-1
    while d % 2 == 0:
        r += 1; d //= 2
    for _ in range(k):
        a = random.randrange(2, n-1)
        x = pow(a, d, n)
        if x in (1, n-1):
            continue
        for __ in range(r-1):
            x = pow(x, 2, n)
            if x == n-1:
                break
        else:
            return False
    return True

# -----------------------------------------------------------------------------
# 2. Generate a random prime of given bit-length
# -----------------------------------------------------------------------------
def generate_prime(bit_length):
    while True:
        p = random.getrandbits(bit_length) | (1 << (bit_length-1)) | 1
        if is_prime(p):
            return p

# -----------------------------------------------------------------------------
# 3. Modular inverse via Extended Euclid
# -----------------------------------------------------------------------------
def modinv(a, m):
    def egcd(a, b):
        if b == 0:
            return (1, 0, a)
        x1, y1, g = egcd(b, a % b)
        return (y1, x1 - (a // b) * y1, g)
    x, y, g = egcd(a, m)
    if g != 1:
        raise Exception(f"No modular inverse for {a} mod {m}")
    return x % m

# -----------------------------------------------------------------------------
# 4. RSA Key Generation (2 primes)
# -----------------------------------------------------------------------------
def generate_keypair(bit_length=1024):
    p = generate_prime(bit_length // 2)
    q = generate_prime(bit_length // 2)
    while q == p:
        q = generate_prime(bit_length // 2)
    n   = p * q
    phi = (p-1)*(q-1)
    e   = 65537
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2
    d = modinv(e, phi)
    return (e, n), (d, n), p, q

# -----------------------------------------------------------------------------
# 5. Multi-prime RSA Key Generation (3 primes)
# -----------------------------------------------------------------------------
def generate_multi_prime_keypair(bit_length=1024, k=3):
    bits = bit_length // k
    primes = [generate_prime(bits) for _ in range(k)]
    while len(set(primes)) < k:
        primes = [generate_prime(bits) for _ in range(k)]
    n = 1
    phi = 1
    for pi in primes:
        n *= pi
        phi *= (pi-1)
    e = 65537
    if gcd(e, phi) != 1:
        raise Exception("e và phi không nguyên tố cùng nhau, chọn lại primes")
    d = modinv(e, phi)
    return (e, n), (d, n), primes

# -----------------------------------------------------------------------------
# 6. Binary Modular Exponentiation (modexp)
# -----------------------------------------------------------------------------
def modexp(base, exponent, mod):
    result = 1
    base %= mod
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exponent >>= 1
    return result

# -----------------------------------------------------------------------------
# 7. Encrypt/Decrypt
# -----------------------------------------------------------------------------
def encrypt(pubkey, message):
    e, n = pubkey
    return [pow(ord(c), e, n) for c in message]

def decrypt(privkey, ciphertext):
    d, n = privkey
    return ''.join(chr(pow(c, d, n)) for c in ciphertext)

# -----------------------------------------------------------------------------
# 8. CRT Decrypt
# -----------------------------------------------------------------------------
def crt_decrypt(privkey, ciphertext, p, q):
    d, n = privkey
    dp = d % (p-1)
    dq = d % (q-1)
    q_inv = modinv(q, p)
    msg = ""
    for c in ciphertext:
        m1 = pow(c, dp, p)
        m2 = pow(c, dq, q)
        h  = (q_inv * (m1 - m2)) % p
        m  = m2 + h * q
        msg += chr(m)
    return msg

# -----------------------------------------------------------------------------
# 9. Primitive Attacks: Trial Division & Pollard’s Rho
# -----------------------------------------------------------------------------
def trial_division(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return (i, n//i)
    return None

def pollards_rho(n):
    if n % 2 == 0:
        return 2
    def f(x): return (x*x + 1) % n
    x = y = 2
    d = 1
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x-y), n)
    return d if d != n else None

# -----------------------------------------------------------------------------
# 10. Demo & Benchmark
# -----------------------------------------------------------------------------
def main():
    # --- 2-prime RSA demo ---
    print("===== 2-Prime RSA Demo =====")
    pub, priv, p, q = generate_keypair(1024)
    e, n = pub; d, _ = priv
    print("Public key (e,n):", pub)
    print("Private key (d,n):", priv)
    print("Primes p, q:", p, q, "\n")

    plaintext = "Hello, ITMO University!"
    print("Plaintext:", plaintext)
    ciphertext = encrypt(pub, plaintext)
    print("Ciphertext:", ciphertext, "\n")

    decrypted = decrypt(priv, ciphertext)
    print("Decrypted (normal):", decrypted)
    decrypted_crt = crt_decrypt(priv, ciphertext, p, q)
    print("Decrypted (CRT):  ", decrypted_crt, "\n")

    # --- Verify modexp matches pow for first char ---
    m0 = ord(plaintext[0])
    c0 = ciphertext[0]
    print("modexp check:", modexp(m0, e, n)==c0, "(should be True)\n")

    # --- Multi-prime RSA demo ---
    print("===== Multi-Prime RSA Demo (3 primes) =====")
    pub2, priv2, primes = generate_multi_prime_keypair(1024, k=3)
    e2, n2 = pub2; d2, _ = priv2
    print("Public key (e,n):", pub2)
    print("Private key (d,n):", priv2)
    print("Primes:", primes, "\n")

    pt2 = "Multi-Prime RSA!"
    print("Plaintext:", pt2)
    ct2 = encrypt(pub2, pt2)
    print("Ciphertext:", ct2, "\n")

    dt2 = decrypt(priv2, ct2)
    print("Decrypted:", dt2, "\n")

    # --- Primitive attacks on small n ---
    print("===== Primitive Attacks on small n =====")
    pub_small, priv_small, p_s, q_s = generate_keypair(32)
    n_s = pub_small[1]
    print("Small n:", n_s)
    td = trial_division(n_s)
    print("Trial division factors:", td)
    pr = pollards_rho(n_s)
    print("Pollard’s Rho factor:", pr, "\n")

    # --- Benchmark performance ---
    print("===== Benchmark (1024-bit) =====")
    t0 = time.time()
    pub_b, priv_b, p_b, q_b = generate_keypair(1024)
    t_key = time.time() - t0
    print(f"Keygen time: {t_key:.3f} s")

    msg = "Benchmark Test"
    t1 = time.time()
    ct_b = encrypt(pub_b, msg)
    t_enc = time.time() - t1
    print(f"Encrypt time: {t_enc:.3f} s")

    t2 = time.time()
    _ = decrypt(priv_b, ct_b)
    t_dec = time.time() - t2
    print(f"Decrypt time (normal): {t_dec:.3f} s")

    t3 = time.time()
    _ = crt_decrypt(priv_b, ct_b, p_b, q_b)
    t_crt = time.time() - t3
    print(f"Decrypt time (CRT):    {t_crt:.3f} s")

if __name__ == "__main__":
    main()
