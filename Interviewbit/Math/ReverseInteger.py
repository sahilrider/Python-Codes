class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        if A>0:
            res=int(str(A)[::-1])
        else:
            res=int(str(A)[0]+str(A)[-1:0:-1])
        # print(res)
        if (-1*(2**31))<=res<=((2**31)-1):
            return res
        else:
            return 0