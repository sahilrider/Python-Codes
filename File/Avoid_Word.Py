def avoid(word,string):
    for i in string:
        if i in word:
            return False
    return True



fin=open('words.txt')
string=str(input('Enter a string:'))
for line in fin:
    word=line.strip()
    if avoid(word,string):
        print(word)
