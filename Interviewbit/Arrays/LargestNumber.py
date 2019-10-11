from functools import cmp_to_key
def func(a,b):
    x = str(a)+str(b)
    y = str(b)+str(a)
    # print(a,b,x,y)
    return 1 if x>=y else -1
 
class Solution:
    # @param A : tuple of integers
    # @return a strings
 
    def largestNumber(self, A):
        sorted_array = sorted(A, key=cmp_to_key(func), reverse=True) 
        # print(sorted_array)
        number = "".join([str(i) for i in sorted_array]) 
        res = number.lstrip('0')
        return res if res else '0'