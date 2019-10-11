class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        B = []
        maxi=A[0]
        for i in A:
            if i>maxi:
                maxi=i
            B.append(maxi)
        
        C = []
        mini=A[-1]
        for i in reversed(A):
            if i<mini:
                mini=i
            C.append(mini)
        C.reverse()
        flag = 0
        a,b = -1,-1
        for i in range(len(A)):
            if B[i]!=C[i]:
                if flag==0:
                    a=i
                    flag=1
                else:
                    b=i
        return [a,b] if a!=-1 or b!=-1 else [-1]