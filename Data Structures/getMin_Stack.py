class Stack(object):
	"""docstring for Stack"""
	def __init__(self):
		super(Stack, self).__init__()
		self.top = -1
		self.maxElem = 50
		self.data = [None for i in range(50)]

	def push(self, value):
		if self.top == self.maxElem-1 :
			print("Stack Overflow")
			return
		self.top+=1
		self.data[self.top] = value

	def pop(self):
		if self.top == -1:
			print("Stack Underflow")
			return
		print("Popped Elem",self.data[self.top])
		self.top-=1

	def peek(self):
		if self.top == -1:
			#print("Empty Stack")
			return None

		return self.data[self.top]

	def printStack(self):
		if self.top == -1:
			print("Empty Stack")
			return
		temp = self.top
		while(temp != -1):
			print(self.data[temp],end =' ')
			temp-=1
		print()

		
if __name__ == '__main__':

	a=[11,23,3,3,1,18]
	minstack = Stack()
	for i in a:
		if(minstack.peek()==None or i<=minstack.peek()):
			minstack.push(i)
	minstack.printStack()

	print("Min elem", minstack.peek())

	t=a.pop()
	if t==minstack.peek():
		minstack.pop()
	print("Min elem", minstack.peek())	

	t=a.pop()
	if t==minstack.peek():
		minstack.pop()
	print("Min elem", minstack.peek())	

