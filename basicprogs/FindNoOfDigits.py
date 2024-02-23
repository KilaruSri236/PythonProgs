n=435734
count=0
for i in str(n):
    count+=1
print(count)

#or
count1=0
while(n>0):
    n=n//10
    count1+=1
print(count1)