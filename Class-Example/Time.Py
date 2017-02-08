class Time:
    '''Represents Time in 24 hour format.
       Attributes: hr,min,sec'''

    def __init__(self,hour=0,minute=0,second=0):
        self.hr=hour
        self.min=minute
        self.sec=second

    def __str__(self):
        return ('%.2d:%.2d:%.2d'%(self.hr,self.min,self.sec))

    def __add__(self,other):
        if isinstance(other,Time):
            return self.add_time(other)
        else:
            return self.increament(other)

    def add_time(self,other):
        '''Adds to given time'''
        second=self.to_sec() + other.to_sec()
        return to_time(second)

    def increament(self,seconds):
        '''Adds seconds to time'''
        seconds+=self.to_sec()
        return to_time(seconds)
    
    def to_sec(self):
        min=self.hr*60 + self.min
        sec=min*60 + self.sec
        return sec

def to_time(sec):
    t=Time()
    t.hr,t.min=divmod(sec,3600)
    t.min,t.sec=divmod(t.min,60)
    return t


def main():
    t1=Time(1,59,3)
    print(t1)
    t2=Time(2,3,4)
    print(t2)
    t3=Time()
    t3=t1+t2
    print(t3)
    t4=Time()
    t4=t1+360
    print(t4)

main()
