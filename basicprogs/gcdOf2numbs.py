#Using inbuilt method
import math
x=35
y=10
print(" The gcd of ",x,"and",y,"is",math.gcd(x,y))

#or

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
if x>y:
    print(" The gcd of ",x,"and",y,"is",gcd(x,y))
else:
    print(" The gcd of ",x,"and",y,"is",gcd(y,x))

    