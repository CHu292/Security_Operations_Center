# des.py

from tables import *

def permute(block, table, block_size):
    result = 0
    for i in range(len(table)):
        bit = (block >> (block_size - table[i])) & 1
        result = (result << 1) | bit
    return result

def left_rotate(val, n):
    return ((val << n) & 0xfffffff) | (val >> (28 - n))

def generate_keys(key):
    key = permute(key, PC1, 64)
    C, D = key >> 28, key & 0xfffffff
    keys = []
    for shift in SHIFT_SCHEDULE:
        C = left_rotate(C, shift)
        D = left_rotate(D, shift)
        keys.append(permute((C << 28) | D, PC2, 56))
    return keys

def sbox_substitute(block):
    output = 0
    for i in range(8):
        segment = (block >> (42 - 6 * i)) & 0x3f
        row = ((segment >> 5) << 1) | (segment & 1)
        col = (segment >> 1) & 0xf
        output = (output << 4) | S_BOX[i][row][col]
    return output

def des_round(L, R, key):
    expanded = permute(R, E, 32)
    x = expanded ^ key
    sbox_result = sbox_substitute(x)
    f_result = permute(sbox_result, P, 32)
    return R, L ^ f_result

def des_block(block, keys, decrypt=False):
    block = permute(block, IP, 64)
    L, R = block >> 32, block & 0xffffffff
    if decrypt:
        keys = keys[::-1]
    for k in keys:
        L, R = des_round(L, R, k)
    return permute((R << 32) | L, FP, 64)

def pad(data):
    pad_len = 8 - (len(data) % 8)
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    return data[:-data[-1]]

def encrypt(data: bytes, key: bytes) -> bytes:
    key_int = int.from_bytes(key, 'big')
    subkeys = generate_keys(key_int)
    data = pad(data)
    return b''.join(
        des_block(int.from_bytes(data[i:i+8], 'big'), subkeys).to_bytes(8, 'big')
        for i in range(0, len(data), 8)
    )

def decrypt(data: bytes, key: bytes) -> bytes:
    key_int = int.from_bytes(key, 'big')
    subkeys = generate_keys(key_int)
    result = b''.join(
        des_block(int.from_bytes(data[i:i+8], 'big'), subkeys, decrypt=True).to_bytes(8, 'big')
        for i in range(0, len(data), 8)
    )
    return unpad(result)
