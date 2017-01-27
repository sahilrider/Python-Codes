def gcd(x,y):
	for i in range (1,min(x,y)+1):
		if x%i==0 and y%i==0:
			cf=i
	return cf
