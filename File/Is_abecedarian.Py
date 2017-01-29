def is_abecedarian(word):
    prev=word[0]
    for nxt in word:
        if nxt < prev:
            return False
        else:
            prev=nxt
    return True

fin=open('words.txt')
for line in fin:
    word=line.strip()
    if is_abecedarian(word):
        print(word)
