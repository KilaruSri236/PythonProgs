n=45

c=0
if n==1:
    print("Not a prime")
else:
    for i in range(2,int(n/2)+1):
        if n%i==0:
            c+=1
    if(c>0):
        print("Not a prime")
    else:
        print("A Prime")