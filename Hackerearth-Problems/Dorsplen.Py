'''https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/dorsplen/'''

li=list(map(int,input().split()))
li.sort()
#print(li)
one=(li[1]-li[0])//2
#print(one)
li[1]=li[1]-2*one
two=(li[2]-li[1])//2
li[2]=li[2]-2*two
#print(two)
print(li[2]+one+two)
