#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/jarvis-and-seven-segments-1/

def led(n):
    if n==1:
        return 2
    elif n==7:
        return 3
    elif n==4:
        return 4
    elif n==5 or n==3 or n==2:
        return 5
    elif n==0 or n==6 or n==9:
        return 6
    elif n==8:
        return 7
     
def tled(n):
    if n==0:
        sum=6
    else:
        sum=0
    while n!=0:
        sum=sum+led(n%10)
        n=int(n/10)
    return sum
   
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=a[0]
    #print(a)
    for j in a:
        if int(tled(ans)) > int(tled(j)):
            ans=j
    print(ans)
