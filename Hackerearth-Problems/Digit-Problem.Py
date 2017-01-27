#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/digit-problem/

a=list(map(int,input().split()))
x=a[0]
k=a[1]
temp=x
len=0
while temp!=0:
    len=len+1
    temp=int(temp/10)
    
len=len-1
while k!=0:
    temp= 9 * 10**len + x% 10**len
    if temp > x%10**(len+1):
        x=x - x%10**(len+1) + temp
        k=k-1
        len=len-1
    else:
        len=len-1
print(x)
