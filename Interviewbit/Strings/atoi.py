class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        res=''
        pos=1
        if A[0]=='+':
            pos=1
        if A[0]=='-':
            pos=0
        for i in range(len(A)):
            if i==0:
                if A[i]=='+' or A[i]=='-':
                    continue
            if A[i]>='0' and A[i]<='9':
                res+=A[i]
            else:
                break
        # print(res)
        if len(res)==0:
            return 0
        if pos==0:
            res = (-1)*int(res)
        else:
            res = int(res)
        if res < -1 *(2**31 -1):
            return -2147483648
        elif res> 2**31:
            return 2147483647
        else:
            return res