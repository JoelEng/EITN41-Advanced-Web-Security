import re
from p2_mgf1 import mgf1
from p2_mgf1 import xor
from hashlib import sha1

def oaep_decode(EM: str) -> str:
  k = 128
  h_len = 20
  h_len_hex = 2 * h_len
  l_hash = sha1(b'').hexdigest()

  masked_seed = EM[2 : h_len_hex + 2]
  masked_db = EM[h_len_hex + 2:]
  seed_mask = mgf1(bytes.fromhex(masked_db), h_len)
  seed = xor(masked_seed, seed_mask)
  db_mask = mgf1(seed, k - h_len - 1)
  db = xor(masked_db, db_mask)
  if db.hex()[:h_len_hex] != l_hash: return "decryption error"
  return re.sub(r"^0*1", "", db.hex()[h_len_hex:])

em = "00581bc2381cf79218566065eb1def452262df368e129de319b5c2bb66e84df6be244fc653a9468c6aafbe715fe366526e9596c452cdf7a42ddcec8d8005724dc7d9450b769aa0fe6f58e8949e503294de3106a7a3b0254eac2b94d245421e610ca70466137c29e7ff5ccd41dda83a44457ea3c820d0f360599833d34ec82e3b"
msg = oaep_decode(em)
print(msg)
