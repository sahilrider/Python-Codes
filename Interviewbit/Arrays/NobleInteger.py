class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        flag = -1
        n = len(A)
        for i in range(n):
            if A[i]==A[i-1] and flag==1:
                flag = -1
            elif flag==1 and A[i]!=A[i-1]:
                break
            if A[i]==(n-i-1):
                flag=1
        return flag