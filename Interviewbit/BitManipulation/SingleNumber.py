class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        res=A[0]
        for i in A[1:]:
            res = res^i
        return res