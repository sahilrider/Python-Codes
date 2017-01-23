def gcd(x,y):
    i=min(x,y)
    while i>=0:
        if x%i==0 and y%i==0:
            return i
        else:
            i=i-1

