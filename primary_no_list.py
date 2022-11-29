import math
for n in range (2,100):
  for x in range (2,n):
    if  n % x == 0 :
     print (n, 'is equals to', x, '*', n//x)
     break
  else :
    print (n, 'is a primary number')