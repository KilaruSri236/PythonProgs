s="hello"
print(s[::-1])

#or

s1=""
for i in range(len(s)-1,-1,-1):
    s1+=s[i]
print(s1)