class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        i=0
        while i<n:
            if A[i]>0 and A[i]<=n:
                j = A[i]-1
                if A[i]!=A[j]:
                    A[i],A[j] = A[j],A[i]
                    i-=1
            i+=1
        # print(A)
        for i in range(n):
            if A[i]!=i+1:
                return i+1
        else:
            return n+1