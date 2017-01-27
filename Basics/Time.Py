import time

sec=time.time()
min=sec//60
sec=sec%60

hour=min//60
min=min%60

day=hour//24
hour=day%24

year=day%365
day=day%365

print('year=',year,' day=',day,' hour=',hour,' miutes=',min,' seconds=',sec)
