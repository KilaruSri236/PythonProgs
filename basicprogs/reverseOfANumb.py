n=346
x=str(n)
print(int(x[::-1]))

#Or

revNumb=0
while(n>0):
    revNumb=revNumb*10+n%10
    n=n//10
print(revNumb)