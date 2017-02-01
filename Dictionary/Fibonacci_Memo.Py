'''Normally any fibonacci function will reach max recurssion depth and will terminate.
   But as in this code we are storing previously know fibonacci no.s in a globally declared dictionary.
   So,It is a much efficient way as it only need two previous no.s
   And because they are stored in dictionary, which uses hash table to store value
   So,searching is also easier'''

'''A previously computed value that is stored for later use is called a memo'''

known={0:0,1:1}

def fib(n):
    if n in known:
        return known[n]
    else:
        res=fib(n-1)+fib(n-2)
        known[n]=res
        return res

n=10
for i in range(1000):
    print(fib(i))
