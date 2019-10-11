class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        a=''
        for i in A:
            o = ord(i)
            if (o>=97 and o<=122) or (o>=48 and o<=57):
                a+=i
            elif o>=65 and o<=90:
                a+=chr(o+32)
        if a==a[::-1]:
            return 1
        else:
            return 0