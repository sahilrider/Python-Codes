class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        l = len(A)
        B = [A[i]+i for i in range(l)]
        C = [A[i]-i for i in range(l)]
        r = max((max(B)-min(B)),(max(C)-min(C)))
        return r