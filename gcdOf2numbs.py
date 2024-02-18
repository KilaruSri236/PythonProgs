#Using inbuilt method
import math
x=int(input("Enter a number"))
y=int(input("Enter another number"))
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

    