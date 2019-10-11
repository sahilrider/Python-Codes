class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        isprime=[1]*(A+1)
        isprime[0],isprime[1]=0,0
 
        i=2
        while(i*i<=A):
            if isprime[i]:
                j=i*2
                while(j<=A):
                    isprime[j]=0
                    j+=i
            i+=1
        for i in range(2,A//2+1):
            if isprime[i] and isprime[A-i]:
                return i,A-i