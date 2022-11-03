def luhn(s: str) -> int:
  x_idx = s[::-1].index("X")
  s = s.replace("X", "0")
  possible_x = 10 - sum(double_nums(s)) % 10
  if possible_x == 10: possible_x = 0
  if x_idx % 2 == 0:
    return possible_x
  elif possible_x % 2 == 0:
    return int(possible_x / 2)
  else:
    x = "".join([str(1), str(possible_x - 1)])
    return int(int(x) / 2)

def double_nums(s: str) -> tuple[list, int]:
  "Doubles every other number. Returns a reverted array"
  new_num = []
  for idx, c in enumerate(s[::-1]):
    if idx % 2 == 1:
      new_c = int(c) * 2
      new_c = shorten_num(new_c)
      new_num.append(new_c)
    else: new_num.append(int(c))
  return new_num

def shorten_num(i: int) -> int:
  "Add together all numbers in an int"
  s = str(i)
  new_num = 0
  for c in s: new_num += int(c)
  return new_num

f = open("p1_luhn.in", "r")
s = f.read()
out = "".join([str(luhn(line)) for line in s.splitlines()])
print(out)
print(int(out) == 5496331440914992338434701218071555719657419448245128019889398009532562488698540071959143506293615978)
f.close()
