def value(r): 
    if (r == 'I'): 
        return 1
    if (r == 'V'): 
        return 5
    if (r == 'X'): 
        return 10
    if (r == 'L'): 
        return 50
    if (r == 'C'): 
        return 100
    if (r == 'D'): 
        return 500
    if (r == 'M'): 
        return 1000
    return -1
    
class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        res = 0
        i = 0
        while(i <len(A)):
            s1 = value(A[i])
            if(i+1 < len(A)):
                s2 = value(A[i+1])
                if s1>=s2:
                    res+=s1
                    i+=1
                else:
                    res = res+s2-s1
                    i+=2
            else:
                res+=s1
                i+=1
        return res