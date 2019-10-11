class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        max_so_far = min(A)
        max_ending_here = 0
        for i in A:
            max_ending_here+=i
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
            if max_ending_here<0:
                max_ending_here = 0
            
        return max_so_far