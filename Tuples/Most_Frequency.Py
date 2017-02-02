def histogram(string):
    d=dict()
    for c in string:
        d[c]=d.get(c,0)+1
    return d                

def most_freq(string):
    h=histogram(string)     #returns a dict(letter,freq)
    t=[]                    #empty list to map dict
    for letter,freq in h.items():
        t.append((freq,letter))         #(freq,letter) is passed as tuple
        
    ''' t is a list of 14 tuples(int,str) in this example'''
    
    t.sort(reverse=True)                #sorting list in desc order by freq

    res=[]                          #list to store only letters
    for freq,x in t:
        res.append(x)
    return res                      #returns a list with letters in desc order of freq

res_seq=most_freq('My name is sahil kumar') #function call returns a list
for x in res_seq:
    print(x)
