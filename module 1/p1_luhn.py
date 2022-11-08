def luhn(s: str) -> int:
  x_idx = s[::-1].index("X")
  s = s.replace("X", "0")
  possible_x = (10 - sum(double_nums(s))) % 10
  if x_idx % 2 == 0:
    return possible_x
  elif possible_x % 2 == 0:
    return int(possible_x / 2)
  else:
    return int((possible_x + 9) / 2)

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
  if i >= 10: return i - 9
  else: return i

f = open("p1_luhn.in")
s = f.read()
f.close()
out = "".join([str(luhn(line)) for line in s.splitlines()])
print(out)
assert(int(out) == 7966652511046784222736055250353099011149212567448299771238329295331001899904649143805478397222467564)
