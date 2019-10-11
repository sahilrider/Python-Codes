class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        res=0
        for i in A:
            res=(res)*26 + (ord(i)-64)
        return res