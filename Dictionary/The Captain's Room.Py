'''https://www.hackerrank.com/challenges/py-the-captains-room'''

k=int(input())
li=list(map(int,input().split()))
a={}
for i in li:
    if i not in a:
        a[i]=1
    else:
        a[i]+=1
for room,freq in sorted(a.items()):
    if freq==1:
        print(room)
        break
