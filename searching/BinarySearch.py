l=[12,24,36,48,56,69]
ele=4
i=0
j=len(l)-1
while(i<=j):
    mid=(i+j)//2
    if ele==l[mid]:
        print("Element found at position ",mid)
        exit()
    elif ele>l[mid]:
        i=mid+1
    else:
        j=mid-1
print("Element not found")

        