s="abccba"
p=1
i=0
j=len(s)-1
while(i<len(s) and j>=0):
    if s[i]!=s[j]:
        p=0
        break
    i+=1
    j-=1
if p==1:
    print("A Palindrome")
else:
    print("Not a Palindrome")

#or:

if s==s[::-1]:
    print("A palindrome")
else:
    print("Not a Palindrome")
