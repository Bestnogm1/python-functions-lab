def sum_to(n) :
  num = 0
  for n in range(1, n + 1) :
    num += n
    return num

def largest(n) :
  return max(n)

def occurrence(o,c) :
  return o.count(c)

def product(*pro) :
  let = 1
  for p in pro :
    let *= p
    return let
print(product(4, 0.5, 5))

