fin=open('words.txt')
total_word=0
no_e=0
for line in fin:
    word=line.strip()
    total_word=total_word+1
    if 'e' not in word:
        print(word)
        no_e=no_e+1

print(no_e/total_word)
