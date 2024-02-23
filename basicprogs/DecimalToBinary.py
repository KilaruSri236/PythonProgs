n=8
binary=""
while(n>0):
    binary+=str(n%2)
    n=n//2
print(binary[::-1])