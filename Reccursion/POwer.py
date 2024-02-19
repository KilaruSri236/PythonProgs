def pow(n,k):
    if k==0:
        return 1
    else:
        return n*pow(n,k-1)
n=10
k=3
print(pow(n,k))