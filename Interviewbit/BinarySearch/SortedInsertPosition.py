'''https://www.interviewbit.com/problems/sorted-insert-position/'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        l, h = 0, len(A)-1
        while(l<=h):
            m = l + (h-l)//2
            # print(l,h,m)
            if (A[m]==B) or (m==0 and B<A[m]) or (m>0 and B<A[m] and B>A[m-1]):
                return m
            elif A[m]>B:
                h = m-1
            else:
                l = m+1
        return len(A)