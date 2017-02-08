class Kangaroo:
    '''Attributes:name,pouch_contents'''

    def __init__(self,name,contents=None):
        self.name=name
        if contents==None:
            self.pouch_contents=[]
        else:
            self.pouch_contents=contents

    def __str__(self):
        t=[self.name+' has pouch contents:']
        for obj in self.pouch_contents:
            s=object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self,item):
        self.pouch_contents.append(item)


def main():
    kanga=Kangaroo('kanga')
    roo=Kangaroo('roo')
    kanga.put_in_pouch('wallet')
    kanga.put_in_pouch('keys')
    kanga.put_in_pouch(roo)

    print(kanga)
    

main()
