n=25
print("The prime factors of ",n," are ")
for i in range(2,n+1):
    if n%i==0:
        j=2
        c=0
        while(j<i):
            if i%j==0:
                c+=1
            j+=1
        if c==0:
            print(i)