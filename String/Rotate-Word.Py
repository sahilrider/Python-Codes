'''Rotate Word means a+1=b z+1=a like that'''

def rotate_letter(letter,n):
    if letter.isupper():
        start=ord('A')
    elif letter.islower():
        start=ord('a')
    else:
        return letter

    val=ord(letter)-start
    i=(val+n)%26+start     #to rotate z+1=a
    return chr(i)


def rotate_word(word,n):
    new=''
    for letter in word:
        new+=rotate_letter(letter,n)
    return new

print(rotate_word('sahil',10))
        
    
