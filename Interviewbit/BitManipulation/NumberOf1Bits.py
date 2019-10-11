class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        r=0
        while(A>0):
            A = A&(A-1)
            r+=1
        return r