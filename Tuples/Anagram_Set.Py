'''Playing With Anagrams'''

def signature(s):
    li=list(s)
    li.sort()
    li=''.join(li)
    return li

'''Signature is a string that contains all of the letters in order.
   print(signature('sahil'))
   output : ahils'''

def all_anagrams(filename):
    d={}   
    fin=open(filename)
    for line in fin:
        word=line.strip().lower()
        t=signature(word)

        if t not in d:
            d[t]=[word]
        else:
            d[t]+=[word]
    return d

def print_anagram_sets_in_order(d):
    '''prints anagram sets in desc order of size'''
    #make a list of (length,word pairs)
    t=[]
    for v in d.values():
        if len(v)>1:
            t.append((len(v),v))

    '''Here, t is a list of tuple(int,list of str)
       in tuple first one is length of 'list of str' and a 'list of str'

       Example:----
       (2,['aah','aha']) is one of the element of t.
       which is tuple.'''
    
    #sort in desc order of length
    t.sort(reverse=True)

    
    for x in t:
        print(x)

def filter_length(d,n):
    '''returns a dict of anagrams having length=n'''
    res={}
    for word,anagram in d.items():
        if len(word)==n:
            res[word]=anagram
    return res
    

if __name__ == '__main__':
    anagram_map = all_anagrams('words.txt')
    print_anagram_sets_in_order(anagram_map)

    eight_letters = filter_length(anagram_map, 8)
    #print_anagram_sets_in_order(eight_letters)
