l=list(map(int,input("Enter the list of elements which has to be sorted").split()))
def SelectionSort(l):
    for i in range(len(l)-1):
        mi=i  
        for j in range(i+1,len(l)):
            if l[mi]>l[j]:
                mi=j
        x=l[mi]
        l[mi]=l[i]
        l[i]=x
    return l
print("After sorting" ,SelectionSort(l))
            