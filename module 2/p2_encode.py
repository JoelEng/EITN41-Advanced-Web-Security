from p2_mgf1 import mgf1
from p2_mgf1 import xor
from hashlib import sha1

def oaep_encode(M: str, seed: str) -> str:
  k = 128
  h_len = 20
  h_len_hex = 2 * h_len
  m_len = int(len(M) / 2) # Byte length is half of the hexadecimal character count
  if m_len > k - 2 * h_len - 2: return "message too long"
  l_hash = sha1(b'').hexdigest()

  ps = "00" * (k - m_len - h_len_hex - 2)
  db = l_hash + ps + "01" + M
  db_mask = mgf1(bytes.fromhex(seed), k - h_len - 1)
  masked_db = xor(db, db_mask)
  seed_mask = mgf1(masked_db, h_len)
  masked_seed = xor(seed, seed_mask)
  return "00" + (masked_seed + masked_db).hex()

msg = "c4254022d53ed188e5156b41397bef79ae81f26e0af26810"
seed = "117d55ae86212ef0c5baca99c2a208d275c6ff00"
em = oaep_encode(msg, seed)
print(em)
