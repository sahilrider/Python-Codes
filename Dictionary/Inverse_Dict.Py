'''If any key-value dictionary is made,
   and we want to make inverse of dictionary.
   A value can have different keys,
   so in inverse dictionary ,
   all keys are stored in a list'''


def make_dict(string):
    d=dict()
    for c in string:
        d[c]=d.get(c,0)+1
    return d

def print_dict(d):
    
    print("Key\tValue")
    for key in d:
        print(key,'\t',d[key])


def inverse_dict(d):
    inverse=dict()
    for key in d:
        val=d[key]
        if val not in inverse:
            inverse[val]=[key]
        else:
            inverse[val].append(key)
    return inverse


string='parrot'
d=make_dict(string)
print("Dictionary:")
print_dict(d)
inv=inverse_dict(d)
print("Inverse Dictionary:")
print_dict(inv)
            
'''-----------------------Output------------
Dictionary:
Key	Value
p 	 1
a 	 1
r 	 2
o 	 1
t 	 1
Inverse Dictionary:
Key	Value
1 	 ['p', 'a', 'o', 't']
2 	 ['r']
'''
