class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        for i in range(0,len(A)-1,2):
            A[i], A[i+1] = A[i+1],A[i]
        return A