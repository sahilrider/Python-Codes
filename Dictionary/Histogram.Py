def histogram(string):
    d=dict()
    for c in string:
        d[c]=d.get(c,0)+1
    return d

def print_hist(h):
    for key in h:
        print(key,h[key])

def print_sorted_hist(h):
    for key in sorted(h):
        print(key,h[key])
        

h=histogram('Hi! This is sahil kumar')
print_hist(h)
print('\n')
print_sorted_hist(h)
