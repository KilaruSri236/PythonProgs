year=1917
if year%4==0:
    if year%100==0 and year%400:
            print("A Leap Year")
    elif(year%100==0):
        print("Not A Leap Year")
    else:
        print("A Leap Year")
else:
    print("Not A Leap Year")