class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        if len(A)==0:
            return 0
 
        l = A.split()
        # print(l)
        if len(l)>0:
            r = l[-1]
        else:
            return 0
        return len(r)