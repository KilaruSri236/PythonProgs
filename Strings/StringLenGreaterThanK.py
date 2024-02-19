s="string having length greater than k"
k=4
res=""
words=s.split(" ")
for i in words:
    if len(i)>k:
        res=res+i+" "
print(res)