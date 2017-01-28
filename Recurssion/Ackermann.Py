'''https://en.wikipedia.org/wiki/Ackermann_function
   It is a non primitive recurssion'''

def A(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return A(m-1,1)
    elif m>0 and n>0:
        return A(m-1,A(m,n-1))

print(A(3,4))
