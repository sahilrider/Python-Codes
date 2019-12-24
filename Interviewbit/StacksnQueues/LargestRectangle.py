'''https://www.interviewbit.com/problems/largest-rectangle-in-histogram/'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        A.append(0)
        stack = [-1]
        res = 0
        for i in range(len(A)):
            while A[i]<A[stack[-1]]:
                h = A[stack.pop()]
                w = i - stack[-1] -1
                res = max(res, h*w)
            stack.append(i)
        A.pop()
        return res