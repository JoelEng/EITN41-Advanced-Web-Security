from hashlib import sha256

def int_to_hex(i: int) -> str:
  return "{0:#0{1}x}".format(i,10)[2:]

def int_to_bytes(i: int) -> bytes:
  return i.to_bytes(4, "big")

def hex_to_int(h: str) -> int:
  return int(h, 16)

def hex_to_bytes(h: str) -> bytes:
  return bytes.fromhex(h)

def bytes_to_int(b: bytes) -> int:
  return int.from_bytes(b, "big")

def bytes_to_hex(b: bytes) -> str:
  return b.hex()

def sha(b: bytes) -> bytes:
  return sha256(b).digest()

def sha_hex(h: str) -> str:
  return sha256(hex_to_bytes(h)).hexdigest()

assert(2022 == bytes_to_int(hex_to_bytes(int_to_hex(2022))))
assert(2022 == hex_to_int(bytes_to_hex(int_to_bytes(2022))))
assert(sha_hex("0123456789abcdef") == bytes_to_hex(sha(hex_to_bytes("0123456789abcdef"))))

# Questions
# print(int_to_hex(8888))                                     # Question 1
# print(bytes_to_hex(sha(int_to_bytes(8888))))                # Question 2, should use sha_hex instead
# print(bytes_to_int(sha(hex_to_bytes("0123456789abcdef"))))  # Question 3, should use sha_hex instead
# print(hex_to_int("0123456789abcdef"))                       # Question 4
