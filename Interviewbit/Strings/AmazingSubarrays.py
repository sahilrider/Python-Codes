class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        m = 10003
        n = len(A)
        ctr = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(n):
            if A[i] in vowels:
                ctr+=n-i
        return ctr%m