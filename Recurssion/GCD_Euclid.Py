def gcdeuclid(x,y):
	#assume x>y
	if x<y:
		(x,y)=(y,x)
	
	rem=x%y
	if (x%y)==0:
		return y
	else:
		return gcdeuclid(y,rem)
