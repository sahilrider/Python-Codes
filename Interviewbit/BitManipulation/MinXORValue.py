class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        A.sort()
        t=[]
        for i in range(len(A)-1):
            t.append(A[i]^A[i+1])
        return min(t)