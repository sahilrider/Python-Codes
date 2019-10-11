class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        res = []
        n1 = len(A)
        n2 = len(B)
        
        i,j = 0,0
        while(i<n1 and j<n2):
            if A[i]==B[j]:
                res.append(A[i])
                i+=1
                j+=1
            elif A[i]>B[j]:
                j+=1
            else:
                i+=1
        return res