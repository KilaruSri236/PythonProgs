n=4
def fibinacci(n):
    if n==0:
        return 0
    if n==1 :
        return 1
    else:
        return fibinacci(n-1)+fibinacci(n-2)
print(fibinacci(n))