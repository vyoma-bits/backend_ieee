import math
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
h=math.gcd(a,b)
l=[c,d,e]
for i in l:
    h=math.gcd(i,h)
print(h)

               

