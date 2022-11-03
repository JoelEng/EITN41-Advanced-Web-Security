from hashlib import sha256

def int_to_hex(num: int) -> bytes:
  return num.to_bytes(4, byteorder="big")

def int_to_arr(num: int) -> list:
  return ""

def hex_to_int(s: str) -> int:
  return int.from_bytes(s.encode(), byteorder="big")

def hex_to_arr(hex: bytes) -> list:
  return ""

def arr_to_int(arr: list) -> int:
  return ""

def arr_to_hex(arr: list) -> bytes:
  return ""

def sha(arr: list) -> int:
  b = sha256(arr).digest()
  return int.from_bytes(b, byteorder="big")
