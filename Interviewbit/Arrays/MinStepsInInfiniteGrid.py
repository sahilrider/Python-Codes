class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        ctr=0
        initx = A[0]
        inity = B[0]
        for i in range(1,len(A)):
            tempx = abs(A[i]-initx)
            tempy = abs(B[i]-inity)
            ctr+= max(tempx,tempy)
            initx, inity = A[i], B[i]
        return ctr