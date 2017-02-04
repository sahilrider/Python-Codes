'''Question 1'''
'''To reverse a number'''
def intreverse(n):
    res=0
    while n>0:
        res=res*10+n%10
        n=n//10
    return res

'''Question 2'''
'''To check the paranthesis'''
def matched(s):
    li=[]
    for i in s:
        if i=='(':
            li.append(i)
        elif i==')':
            if len(li)==0:
                return False
            else:
                p=li.pop()
                if p is not '(':
                    return False
    if len(li)==0:
        return True
    else:
        return False
    
'''Question 3'''
'''To find the sum of all prime in a list'''
def isprime(n):
    if n<=1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1

def sumprimes(li):
    res=0
    for i in li:
        if isprime(i):
            res+=i
    return res



'''Demonstration
>>> intreverse(783)
387
>>> intreverse(242789)
987242
>>> intreverse(3)
3

>>> matched("zb%78")
True
>>> matched("(7)(a")
False
>>> matched("a)*(?")
False
>>> matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")
True

>>> sumprimes([3,3,1,13])
19
>>> sumprimes([2,4,6,9,11])
13
>>> sumprimes([-3,1,6])
0
'''
