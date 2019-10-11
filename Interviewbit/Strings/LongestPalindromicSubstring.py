class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        maxlen = 1
        s = 0
        l = len(A)
        
        low,high = 0,0
        
        for i in range(1,l):
            low = i-1
            high = i
            while low>=0 and high<l and A[low]==A[high]:
                if high-low+1 > maxlen:
                    s=low
                    maxlen = high-low+1
                low-=1
                high+=1
            
            low,high = i-1, i+1
            while low>=0 and high<l and A[low]==A[high]:
                if high-low+1 > maxlen:
                    s = low
                    maxlen = high-low+1
                low-=1
                high+=1
            # print(A[s:s+maxlen], s,maxlen)
        return A[s:s+maxlen]