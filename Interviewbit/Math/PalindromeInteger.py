class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        A=str(A)
        if A==A[::-1]:
            return 1
        else:
            return 0