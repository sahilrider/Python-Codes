'''https://www.interviewbit.com/problems/square-root-of-integer/'''

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A==1:
            return 1
        l, h = 1, A
        m = A/2
        i = 0
        while(l<=h and i!=50):
            # print(m, l, h)
            if m*m == A:
                return m
            elif m*m >A:
                h = m
            else:
                l = m
            m = (l+h)/2    
            i+=1
        return m