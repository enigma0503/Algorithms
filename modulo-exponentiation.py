import math
def exponentialOfTwo(x):
  exList = []
  while x >= 2:
    ex = int(math.log(x, 2))
    exList.append(ex)
    #print("ex == "+str(ex))
    x -= 2 ** ex
    #print("x == "+str(x))
    if x == 1:
      exList.append(0)
  return exList

def cal(b,e,n):
  ls = exponentialOfTwo(e)
  #print (ls)
  mi = min(ls)
  mx = max(ls)
  #print (mi , mx)
  val = 1
  c = b%n
  if (mi ==0):
    val = b%n
  for i in range (1,mx+1):
    #print("i == " + str(i))
    c = (c*c)%n
    if ( i in ls ):
      #print ("c == " + str(c))
      val *=c
      #print ("val == "+str(val))

  return (val%n)


print(cal(25, 99, 230))
