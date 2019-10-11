class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
       n=len(A)
       if len(A)==0:
            return ''
       elif len(A)==1:
           return A[0]
       A.sort()
       end = min(len(A[0]), len(A[n-1]))
       i=0
       while i<end:
           if A[0][i] == A[n-1][i]:
               i+=1
           else:
               break
       return A[0][:i]