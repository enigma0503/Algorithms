def extended_gcd(a, b):
  assert a >= b and b >= 0 and a + b > 0
  if b == 0:
    d, x, y = a, 1, 0
  else:
    (d, p, q) = extended_gcd(b, a % b)
    x = q
    y = p - q * (a // b)

  assert a % d == 0 and b % d == 0
  assert d == a * x + b * y
  return (d, x, y)

def diophantine(a, n, c):
  flag = 0
  if (a<n):
    a,n = n,a
    flag = 1
  (d,x,y) = extended_gcd(a,n)
  if (flag==1):
    x,y = y,x
    
  return (x*(c//d), y*(c//d))

  
def divide(a, b, n):
  assert n > 1 and a > 0
  (x,y) = diophantine(a, n, 1)
  x = x % n
  ans = (b*x)%n
  return ans

print(divide(17,1,43))
