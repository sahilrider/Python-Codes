class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        B = []
        A.reverse()
        flag=0
        first=1
        for i in range(len(A)):
            # print(i,B)
            if i==1:
                first=0
            if first:
                if A[i]==9:
                    B.append(0)
                    flag=1
                else:
                    B.append(A[i]+1)
                    flag=0
            else:
                if flag==0:
                    B.extend(A[i:])
                    break
                else:
                    if A[i]==9:
                        B.append(0)
                        flag=1
                    else:
                        B.append(A[i]+1)
                        flag=0
        if flag==1:
            B.append(1)
        B.reverse()
        B=int(''.join(map(str,B)))
        B = list(map(int, str(B))) 
        return B