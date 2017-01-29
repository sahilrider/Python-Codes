def uses_only(word,string):
    for letter in word:
        if letter not in string:
            return False
    return True

fin=open('words.txt')
string=str(input('Enter a string:'))
for line in fin:
    word=line.strip()
    if uses_only(word,string):
        print(word)
