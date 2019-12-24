'''interviewbit.com/problems/implement-power-function/'''

def f(x,n,d):
    if x==0:
            return 0
    if n==0:
        return 1
    #even
    res = 0
    if(n%2==0):
            res = f(x,n//2,d)
            res = (res * res)%d
    else:
        res = x%d
        res = (res * f(x, n-1, d)%d)%d
    return ((res+d)%d)
class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        return f(x,n,d)
        
            