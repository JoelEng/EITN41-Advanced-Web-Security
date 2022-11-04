from hashlib import sha1
from p1_data_conversion import hex_to_bytes

def hash(arr: list) -> str:
  hash = ""
  for line in arr:
    hash = hashNode(hash, line)
  return hash

def hashNode(prev: str, node: str) -> str:
  if node[0] == "L":
    a = node[1:] + prev
  elif node[0] == "R":
    a = prev + node[1:]
  else:
    return node # Avoid hashing the first leaf
  return sha1(hex_to_bytes(a)).hexdigest()

f = open("p2_spv.in")
arr = f.read().splitlines()
f.close()
print(hash(arr))
