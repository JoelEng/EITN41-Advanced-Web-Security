from hashlib import sha1

iden = "faythe@crypto.sec"
p = "9240633d434a8b71a013b5b00513323f"
q = "f870cfcd47e6d5a0598fc1eb7e999d1b"

encr_bits = """48ac2b789772fa3182555a10679ac8b34d200fddd35e6c2cbdc6138a14745eb6
062d1d1747b964c475b95fdc06e98b2cabf4bea3309b1445988ece98900e1faf
7afa27f7d38c8fcb8e2c3c1863482fffa7b9362813a90241a219961b90ddf523
039e27d3bb54b752f6fd4154b0af24a1d838e1bef927fedabed4bcde43e4dab6
1b0d59f709e371c2d76b914be5b0fb2c678dbd2cc72724e96f7df1138bb326e8
7cfa8b6dfaec9cc0a95795405f042fb9794f4ba23183c9562a298351bf60b2d9
43eff7d8d8a70d8f3597fa9edbcad5b6fd6622683104c60f32475f4a5cfbfdfe
5ac3a317e0a3226f3abfadf98667b3ef03bd285000b1a51f762c39f92db461d0"""

p = int(p, 16)
q = int(q, 16)
m = p * q

def hash_a(a):
  return sha1(a).digest()

def jacobi(a, m):
  res = 1
  a %= m
  while a:
    b = 0
    while not a % 2:
      a //= 2 # integer division because python is weird
      b += 1
    if b % 2 and m % 8 in (3, 5):
      res *= -1
    if a % 4 == m % 4 == 3:
      res *= -1
    a, m = m, a
    a %= m
  if m == 1:
    return res
  return 0

a = hash_a(iden.encode("utf-8"))
while jacobi(int.from_bytes(a, "big"), m) != 1:
  a = hash_a(a)
print("a:", a.hex())

r = pow(int.from_bytes(a, "big"), (m + 5 - p - q) // 8, m)
print("r:", "{0:#0{1}x}".format(r,10)[2:])

bin_res = ""
for si in encr_bits.splitlines(): # decrypt message, each line is an encrypted bit
  if jacobi(int(si, 16) + 2 * r, m) == 1:
    bin_res += "1"
  else: bin_res += "0"

print("message:", int(bin_res, 2))