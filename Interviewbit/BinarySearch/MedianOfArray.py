'''https://www.interviewbit.com/problems/median-of-array/'''

def func(A,B):
    m, n = len(A), len(B)
    if(m<n):
        return func(B,A)
    l, h = 0, 2*n
    while(l<=h):
        mid = l + (h-l)//2
        mid1= m+n -mid
        l1 = float('-inf') if(mid1==0) else A[(mid1-1)//2]
        l2 = float('-inf') if(mid==0) else B[(mid-1)//2]
        r1 = float('inf') if(mid1==m*2) else A[(mid1)//2]
        r2 = float('inf') if(mid==n*2) else B[(mid)//2]
        
        # print(l1,l2,r1,r2)
        # print((max(l1,l2)+min(r1, r2))/2.0)
        
        # print(type((max(l1,l2)+min(r1, r2))/2))
        if l1>r2:
            l = m+1
        elif l2>r1:
            h = m-1
        else:
            r = (max(l1,l2)+min(r1, r2))/2.0
            print(r)
            return r
            
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        r = func(A,B)
        print(r)
        return r
