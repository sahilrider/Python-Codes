'''https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/chandu-and-consecutive-letters/'''

n=int(input())
for i in range(n):
    s=input()
    li=[s[0]]
    for j in range(1,len(s)):
        if s[j]!=s[j-1]:
            li.append(s[j])
    print(''.join(li))
