import numpy.polynomial.polynomial as poly

def get_secret(helpers: list, master_points: list):
  res = 0
  for i, h in enumerate(helpers):
    share = master_points[i]
    delta = get_delta(h, helpers)
    res += delta * share
  return int(res)

def get_delta(i: int, l: list) -> int:
  delta = 1
  for j in l:
    if i == j: continue
    delta *= j / (j - i)
  return delta

k = 5
n = 8
private_polynomial = [13, 8, 11, 1, 5] # Defines your polynomial
other_shares = [75, 75, 54, 52, 77, 54, 43] # Shares recieved from others
helpers = [1, 2, 4, 5, 7] # Accomplices
p = sum([int(poly.polyval(1, private_polynomial))] + other_shares)
master_points = [p, 2782, 30822, 70960, 256422] # All known points on the master polynomial

print(get_secret(helpers, master_points))
assert(get_delta(1, [1, 4]) == 4 / 3)
assert(get_delta(4, [1, 4]) == - 1 / 3)
assert(k == len(helpers) == len(master_points) == len(private_polynomial))
assert(n == len(other_shares) + 1)