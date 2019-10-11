class Solution:
    # @param A : list of integers
    # @return an integer
    # 11 5 9 6 8 6 4 6 9 5 4 9
    def maxSpecialProduct(self, A):
        l = len(A)
        L = [0]
        R = [0]
        m = 1000000007
        
        stack1 = [0]
        top1 = 0
        for i in range(1,l):
            while(top1!=-1):
                if A[i]>=A[stack1[top1]]:
                    stack1.pop()
                    top1-=1
                else:
                    break
            if top1!=-1:
                L.append(stack1[top1])
            else:
                L.append(0)
            stack1.append(i)
            top1+=1
        # print(L)
        
        stack2 = [l-1]
        top2 = 0
        for i in range(l-2,-1,-1):
            while(top2!=-1):
                if A[i]>=A[stack2[top2]]:
                    stack2.pop()
                    top2-=1
                else:
                    break
            if top2!=-1:
                R.append(stack2[top2])
            else:
                R.append(0)
            stack2.append(i)
            top2+=1
        R.reverse()
        # print(R)
        P=[L[i]*R[i] for i in range(l)]
        # print(P)
        return max(P)%m