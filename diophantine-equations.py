def extended_gcd(a, b):
  assert a >= b and b >= 0 and a + b > 0
  if b == 0:
    d, x, y = a, 1, 0
  else:
    (d, p, q) = extended_gcd(b, a % b)
    #print(d,p,q)
    x = q
    y = p - q * (a // b)

  assert a % d == 0 and b % d == 0
  assert d == a * x + b * y
  return (d, x, y)

def diophantine(a, b, c):
  flag = 0
  if (a<b):
    a,b = b,a
    flag = 1
  (d,x,y) = extended_gcd(a,b)
  assert c % d == 0
  # return (x, y) such that a * x + b * y = c
  if (flag==1):
    x,y = y,x  
  return (x*(c//d), y*(c//d))
