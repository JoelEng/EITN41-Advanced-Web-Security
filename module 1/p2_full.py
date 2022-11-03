from hashlib import sha1
from p1_data_conversion import hex_to_bytes
from math import log2

def hash_line(arr: list):
  if len(arr) % 2 != 0:
    arr.append(arr[-1]) # Pad to even length
  add_to_path(arr)
  new_arr = [sha1(hex_to_bytes(a + b)).hexdigest() for (a, b) in pairs(arr)]
  set_new_i()
  return new_arr

def set_new_i():
  global i
  if i % 2 == 0: i = int(i / 2)
  else: i = int((i - 1) / 2)

def add_to_path(arr: list):
  if i % 2 == 0: path_to_i.append("R" + arr[i + 1])
  else: path_to_i.append("L" + arr[i - 1])

def pairs(arr: list) -> list:
  "Each tuple in returned list is two successive input elems"
  a = iter(arr)
  return zip(a, a)

f = open("p2_full.in")
i = int(f.readline())
j = int(f.readline())
path_to_i = []
arr = f.read().splitlines()
f.close()

for _ in range(int(log2(len(arr))) + 1):
  arr = hash_line(arr)

print(path_to_i[-j] + arr[0])
