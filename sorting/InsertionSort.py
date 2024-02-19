def InsertionSort(l):
    for i in range(1,len(l)):
        k=l[i]
        j=i-1
        while(j>=0 and k<l[j]):
            l[j+1]=l[j]
            j-=1
        l[j+1]=k
    return l
l=[23,89,56,1,90]
print(InsertionSort(l))
        
    