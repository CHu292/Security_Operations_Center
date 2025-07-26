#!/usr/bin/env python3
import argparse
import hashlib
import hmac
import sys

def sha256_hash(data: bytes) -> str:
    """Compute SHA-256 of the data and return the hex string."""
    return hashlib.sha256(data).hexdigest()

def verify_sha256_hash(data: bytes, expected_hex: str) -> bool:
    """Verify whether SHA-256 of the data matches the expected hex value."""
    return sha256_hash(data) == expected_hex.lower()

def hmac_sha256(key: bytes, data: bytes) -> str:
    """Generate HMAC-SHA256 from key and data, return the hex string."""
    block_size = hashlib.sha256().block_size
    if len(key) > block_size:
        key = hashlib.sha256(key).digest()
    key = key.ljust(block_size, b'\x00')
    o_key = bytes((b ^ 0x5C) for b in key)
    i_key = bytes((b ^ 0x36) for b in key)
    inner = hashlib.sha256(i_key + data).digest()
    return hashlib.sha256(o_key + inner).hexdigest()

def verify_hmac_sha256(key: bytes, data: bytes, expected_hex: str) -> bool:
    """Verify whether HMAC-SHA256 of the data with the key matches expected_hex."""
    calc = hmac_sha256(key, data)
    # secure comparison
    return hmac.compare_digest(calc, expected_hex.lower())

def load_data(args) -> bytes:
    if args.file:
        return open(args.file, 'rb').read()
    else:
        return args.message.encode()

def main():
    p = argparse.ArgumentParser(
        description="Tool for SHA-256 hashing and HMAC-SHA256 generation/verification")
    sub = p.add_subparsers(dest='cmd', required=True)

    # sha256
    ph = sub.add_parser('hash', help='Compute SHA-256')
    ph.add_argument('-m', '--message', help='Input string', default='')
    ph.add_argument('-f', '--file', help='Input file')

    pv = sub.add_parser('verify-hash', help='Verify SHA-256')
    pv.add_argument('-m', '--message', help='Input string', default='')
    pv.add_argument('-f', '--file', help='Input file')
    pv.add_argument('-s', '--sha', help='Expected SHA-256 value', required=True)

    # hmac
    pm = sub.add_parser('hmac', help='Generate HMAC-SHA256')
    pm.add_argument('-k', '--key', help='HMAC key', required=True)
    pm.add_argument('-m', '--message', help='Input string', default='')
    pm.add_argument('-f', '--file', help='Input file')

    pv2 = sub.add_parser('verify-hmac', help='Verify HMAC-SHA256')
    pv2.add_argument('-k', '--key', help='HMAC key', required=True)
    pv2.add_argument('-m', '--message', help='Input string', default='')
    pv2.add_argument('-f', '--file', help='Input file')
    pv2.add_argument('-t', '--tag', help='Expected HMAC value', required=True)

    args = p.parse_args()
    data = load_data(args)

    if args.cmd == 'hash':
        print(sha256_hash(data))
    elif args.cmd == 'verify-hash':
        ok = verify_sha256_hash(data, args.sha)
        print("OK" if ok else "FAIL")
        sys.exit(0 if ok else 1)
    elif args.cmd == 'hmac':
        key = args.key.encode()
        print(hmac_sha256(key, data))
    elif args.cmd == 'verify-hmac':
        key = args.key.encode()
        ok = verify_hmac_sha256(key, data, args.tag)
        print("OK" if ok else "FAIL")
        sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()

