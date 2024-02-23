n=25
sum=0
for i in range(1,n):
    if n%i==0:
       sum+=i
if sum==n:
    print("A Perfect Number")
else:
    print("Not a perfect number")