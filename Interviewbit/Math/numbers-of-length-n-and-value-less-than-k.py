MAX=10
 
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        d, d2 = 0,0
      
        # Convert number to digit array 
        digit = list(map(int,str(C)))
        d = len(A) 
      
        # Case 1: No such number possible as the 
        # generated numbers will always 
        # be greater than C 
        if (B > len(digit) or d == 0): 
            return 0
      
        # Case 2: All integers of length B are valid 
        # as they all are less than C 
        elif (B < len(digit)): 
            # contain 0 
            if (A[0] == 0 and B != 1): 
                return (d - 1) * pow(d, B - 1) 
            else: 
                return pow(d, B) 
      
        # Case 3 
        else : 
            dp=[0 for i in range(B + 1)] 
            lower=[0 for i in range(MAX + 1)] 
      
            # Update the lower[] array such that 
            # lower[i] stores the count of elements 
            # in A[] which are less than i 
            for i in range(d): 
                lower[A[i] + 1] = 1
            for i in range(1, MAX+1): 
                lower[i] = lower[i - 1] + lower[i] 
      
            flag = True
        dp[0] = 0
        for i in range(1, B+1): 
            d2 = lower[digit[i - 1]] 
            dp[i] = dp[i - 1] * d 
  
            # For first index we can't use 0 
            if (i == 1 and A[0] == 0 and B != 1): 
                d2 = d2 - 1
  
            # Whether (i-1) digit of generated number 
            # can be equal to (i - 1) digit of C 
            if (flag): 
                dp[i] += d2 
  
            # Is digit[i - 1] present in A ? 
            flag = (flag & (lower[digit[i - 1] + 1] == lower[digit[i - 1]] + 1)) 
          
        return dp[B] 