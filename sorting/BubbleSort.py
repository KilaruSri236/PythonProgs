l=[4,2,67,89,23,45,10,6]
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            x=l[i]
            l[i]=l[j]
            l[j]=x
print("The sorted list is ",l)