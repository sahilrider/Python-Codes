class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, arr):
        if len(arr) == 0 or len(arr[0])==0:
            return arr
        
        rows = len(arr)
        cols = len(arr[0])
        
        for r in range(len(arr)):
            for c in range(r, len(arr[0])):
                temp = arr[r][c]
                arr[r][c] = arr[c][r]
                arr[c][r] = temp
         
        for row in arr:
            row = row.reverse()
        
        return arr