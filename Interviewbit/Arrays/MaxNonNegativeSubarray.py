class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        B = []
        idx=0
        for i in range(len(A)):
            if A[i]<0:
                B.append(A[idx:i])
                idx = i+1
            if A[i]>=0 and i==len(A)-1:
                B.append(A[idx:i+1])
        # print(B)
        res = 0
        l = 0
        idx = 0
        for i in range(len(B)):
            temp=sum(B[i])
            if temp>res:
                res=temp
                idx = i
                l=len(B[i])
            if temp==res:
                if len(B[i])>l:
                    l = len(B[i])
                    idx = i
            # print(temp,l,idx)
        # print(B[idx])
        return B[idx]