class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        ctr=0
        n=5
        while(A/n>=1):
            ctr+=int(A/n)
            n*=5
        return ctr