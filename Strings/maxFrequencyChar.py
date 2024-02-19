s="aaaabciuuuffe"
s1=""
l={}
for i in s:
    if i in s1:
        l[i]+=1
    else:
        l[i]=1
        s1+=i
m=max(l.values())

for key,value in l.items():
    if value==m:
        print(key)