n=153
numb=n
m=0
if n==0:
    print("1")
while(n>0):
    x=n%10
    n//=10
    m=m+(x**len(str(numb)))
if m==numb:
    print("armstrong")
else:
    print("Not an armstrong")