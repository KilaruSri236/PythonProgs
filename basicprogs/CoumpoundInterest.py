def CompoundInterest(p,t,r):
    amount=p*((1+r/100)**t)
    return amount-p
p=10000
t=2
r=5
print(CompoundInterest(p,t,r))