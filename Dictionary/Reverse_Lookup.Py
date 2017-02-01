def print_dict(h):
    for key in h:
        print(key,h[key])
        
def rev_lookup(d,val):
    for key in d:
        if d[key]==val:
            return key
    raise LookupError()
    
d={'apple':2,'orange':3,'guava':3}
print_dict(d)
key=rev_lookup(d,3)
print(key)


'''For any value ,there can be more than one key.
So, the first key which is in dictionary will be returned
else 
we raise a lookuperror which means there is no key associated with that value.'''
