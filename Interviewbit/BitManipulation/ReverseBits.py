class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        s=bin(A)[2:].zfill(32)
        r = int(s[::-1],2)
        return r