l=[23,56,3,89,67]
#Using in-built methods
print("The minimum element in the given list is ",min(l))
print("The maximum element in the given list is ",max(l))

#Without using in-built methods
mi=999999
ma=0
for i in l:
    if mi>i:
        mi=i
    if ma<i:
        ma=i
print("The minimum element in the given list is ",mi)
print("The maximum element in the given list is ",ma) 