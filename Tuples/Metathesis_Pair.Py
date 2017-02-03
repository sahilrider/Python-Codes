'''Two words form a “metathesis pair” if you can transform one into the other by
   swapping two letters;
   for example, “converse” and “conserve”.'''

import Anagram_set
from structshape import structshape

def metathesis_pairs(d):
    for anagrams in d.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if word1<word2 and word_diff(word1,word2)==2:
                    print(word1,word2)
                    

def word_diff(word1,word2):
    '''Compute the number of differences between two words'''

    assert len(word1)==len(word2)       #checks if length of both words are True which is hopefully true
                                        #otherwise raise a Assertion error
    count=0
    '''Zip is an object which acts as an iterator in tuple(word1,word2)'''
    for c1,c2 in zip(word1,word2):
        if c1!=c2:
            count+=1
    return count


sets=Anagram_set.all_anagrams('words.txt')
metathesis_pairs(sets)
    
    
    
