from hashlib import sha1

def mgf1(mgf_seed: bytes, mask_len: int) -> str:
  if mask_len > 2 ** 32: return "mask too long"
  mask_len_hex = mask_len * 2 # Since we're dealing with hex strings
  h_len = 20 # Doesn't work when this is changed
  t = ""
  for c in range(int(mask_len / h_len + 1)):
    oct_c = int_to_octet(c, 4)
    t += sha1(mgf_seed + oct_c).hexdigest()
  return t[:mask_len_hex]

def int_to_octet(i: int, x_len: int) -> str:
  return i.to_bytes(x_len, "big") # Same as m1p1 int_to_bytes

def xor(h0: str, h1: str) -> bytes:
  return bytes(a ^ b for (a, b) in zip(bytes.fromhex(h0), bytes.fromhex(h1)))

# print(mgf1(bytes.fromhex("601c47ea27444ce24417a1526c8c65ca8c3191f9877343c202"), 25))