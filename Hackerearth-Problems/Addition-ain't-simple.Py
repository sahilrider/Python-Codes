'''https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/addition-aint-simple/'''

def sum_letter(a,b):
    start=96
    vala=ord(a)-start
    valb=ord(b)-start
    
    i=(vala+valb)%26+start   
    #print(vala,valb,i)
    if(i==96):
        return 'z'
    return chr(i)


def sum(word,word2):
    new=''
    for i in range(len(word)):
        new+=sum_letter(word[i],word2[i])
    return new


n=int(input())
for i in range(n):
    word=str(input())
    word2=word[::-1]
    res=sum(word,word2)
    print(res)
    
    
