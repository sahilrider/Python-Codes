def computeLps(s):
    M = len(s)
    lps = [None] * M
    length = 0
    lps[0] = 0
    
    i = 1
    while(i<M):
        if s[i]==s[length]:
            length+=1
            lps[i]=length
            i+=1
        else:
            if length !=0:
                length = lps[length-1]
            else:
                lps[i]=0
                i+=1
    return lps  
class Solution:
    # @param A : string
    # @return an integer
 
    
    def solve(self, A):
        n = len(A)
        s = A + '$' + A[::-1]
        lps = computeLps(s)
        # print(lps)
        return n - lps[-1]