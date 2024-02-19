def sumOfDigits(n):
    if n<10:
        return n
    else:
        return n%10+sumOfDigits(n//10)
n=146
print(sumOfDigits(n))