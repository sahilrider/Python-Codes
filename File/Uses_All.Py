def uses_all(word,string):
    for letter in string:
        if letter not in word:
            return False
    return True

fin=open('words.txt')
string=str(input('Enter a string:'))
for line in fin:
    word=line.strip()
    if uses_all(word,string):
        print(word)
