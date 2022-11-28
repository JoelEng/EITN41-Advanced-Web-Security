import numpy.polynomial.polynomial as poly

def get_secret(helpers: list, master_points: list):
  res = 0
  for i, h in enumerate(helpers):
    delta = get_delta(h, helpers)
    res += delta * master_points[i]
  return int(res)

def get_delta(i: int, l: list) -> int:
  delta = 1
  for j in l:
    if i == j: continue
    delta *= j / (j - i)
  return delta

k, n = 4, 7
priv_poly = [3, 5, 10, 11] # Defines your polynomial
shares = [45, 39, 41, 55, 45, 41] # Shares recieved from others
helpers = [1, 3, 5, 6] # Accomplices
p = sum([int(poly.polyval(1, priv_poly))] + shares)
master_points = [p, 3313, 12939, 21430] # All known points on the master polynomial

print(get_secret(helpers, master_points))
assert(get_delta(4, [1, 4]) == - 1 / 3)
assert(k == len(helpers) == len(master_points) == len(priv_poly))
assert(n == len(shares) + 1)

print("Question 9:", int(poly.polyval(0, poly.polyfit([1, 2, 3, 4], [0, 2, 4, 10], 3))))
