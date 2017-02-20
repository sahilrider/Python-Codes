'''Question 1'''
def orangecap(d):
    res={}
    for val in d.values():
        for plyr,scr in val.items():
            if plyr not in res:
                res[plyr]=scr
            else:
                res[plyr]+=scr
    k=max(res,key=res.get)
    return (k,res[k])
    
    
'''
Example:
>>> orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}})
('player3', 100)

>>> orangecap({'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'ashwin':59, 'Pujara':42}})
('Kohli', 120)'''


'''Question 2'''

def del0(d):
    '''Fuction to delete terms with zero coefficient'''
    res={}
    for key,val in d.items():
        if val!=0:
            res[key]=val
    return res

def format(d):
    '''Fuction to convert dictionary into list as per decreasing power'''
    li=[]
    for key,val in sorted(d.items(),reverse=True):
        li.append((val,key))
    return li

def multpoly(p1,p2):
    '''Fuction to multiply two polynomial'''
    res={}
    for exp1,pwr1 in p1:
        for exp2,pwr2 in p2:
            if pwr1+pwr2 not in res:
                res[pwr1+pwr2]=exp1*exp2
            else:
                res[pwr1+pwr2]+=exp1*exp2
    res=del0(res)       
    return(format(res))
  
def addpoly(p1,p2):
    '''Function to add two polynomial'''
    res={}
    for exp1,pwr1 in p1:
        for exp2,pwr2 in p2:
            if pwr1==pwr2:
                res[pwr1]=exp1+exp2
    for exp,pwr in p1:
        if pwr not in res:
            res[pwr]=exp
    for exp,pwr in p2:
        if pwr not in res:
            res[pwr]=exp
    res=del0(res)
    return(format(res))
    
    
'''
Example:
>>> addpoly([(4,3),(3,0)],[(-4,3),(2,1)])
[(2, 1),(3, 0)]

Explanation: (4x^3 + 3) + (-4x^3 + 2x) = 2x + 3

>>> addpoly([(2,1)],[(-2,1)])
[]

Explanation: 2x + (-2x) = 0

>>> multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])
[(1, 3),(-1, 0)]

Explanation: (x - 1) * (x^2 + x + 1) = x^3 - 1
'''
