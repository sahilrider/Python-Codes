'''https://www.interviewbit.com/problems/rain-water-trapped/'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        h = max(A)
        highest = A.index(h)
        w = 0
        t = 0
        for i in range(highest):
            # print(i)
            if A[i]>t:
                t = A[i]
            else:
                w+= t - A[i]
        t = 0
        for i in range(len(A)-1,highest,-1):
            # print(i)
            if A[i]>t:
                t = A[i]
            else:
                 w+= t - A[i]
        return w