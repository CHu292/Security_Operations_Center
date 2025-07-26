user = bytearray(b"5zgw95y4")
pwd = bytearray(b"4L4N<L|0")

for i in range(8):
    d = user[i] ^ pwd[i]
    if 48 <= d <= 59:
        print(chr(d), end='')
        continue
    if 97 <= d <= 123:
        print(chr(d), end='')
        continue
    if 80 <= d <= 89:
        print(d - 80, end='')
        continue
    else:
        print(chr(ord('a') - 1 + d), end='')
        continue
