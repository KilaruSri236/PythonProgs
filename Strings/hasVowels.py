s="hello"
def hasVowels(s):
    for i in s.lower():
        if i in "aeiou":
            print("Has vowels")
            return
    return -1
if hasVowels(s)==-1:
    print("No Vowels")
    
    
    