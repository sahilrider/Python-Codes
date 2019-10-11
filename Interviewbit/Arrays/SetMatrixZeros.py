class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        is_col = False
        R=len(A)
        C=len(A[0])
        for i in range(R):
            if A[i][0]==0:
                is_col=True
            for j in range(1,C):
                if A[i][j]==0:
                    A[0][j]=0
                    A[i][0]=0
        for i in range(1,R):
            for j in range(1,C):
                if not A[i][0] or not A[0][j]:
                    A[i][j]=0
        if A[0][0]==0:
            for j in range(C):
                A[0][j]=0
        if is_col:
            for i in range(R):
                A[i][0]=0
        return A