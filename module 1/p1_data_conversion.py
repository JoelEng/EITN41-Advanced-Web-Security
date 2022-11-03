from hashlib import sha256

def int_to_hex(i: int) -> str:
  return "{0:#0{1}x}".format(i,10)[2:]

def int_to_bytes(i: int) -> bytes:
  return int.to_bytes(i, 4, "big")

def hex_to_int(h: str) -> int:
  return int(h, 16)

def hex_to_bytes(h: str) -> bytes:
  return bytes.fromhex(h)

def bytes_to_int(b: bytes) -> int:
  return int.from_bytes(b, "big")

def bytes_to_hex(b: bytes) -> str:
  return b.hex()

def sha(b: bytes) -> bytes: # Doesn't work for question 2
  return sha256(b).digest()

# print(bytes_to_int(hex_to_bytes(int_to_hex(2022))))
# print(hex_to_int(bytes_to_hex(int_to_bytes(2022))))

# print(bytes_to_hex(sha(int_to_bytes(8888))))
