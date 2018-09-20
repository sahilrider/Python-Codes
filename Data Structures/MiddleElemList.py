#Node class
class Node(object):
	"""docstring for Node"""
	def __init__(self, data):
		super(Node, self).__init__()
		self.data = data
		self.next = None

#Linked List class
class LinkedList(object):
	"""docstring for LinkedList"""
	def __init__(self):
		super(LinkedList, self).__init__()
		self.head = None

	"""Inserting new node at the beginning"""
	def push(self, data):

		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	"""Print linked list"""
	def printList(self):

		if self.head == None:
			print("List is empty!!!")
			return

		temp = self.head
		while temp!=None:
			print(temp.data,end=" ")
			temp = temp.next
		print()

	def printMiddle(self):
		fast = self.head 
		mid = self.head
		ctr = 0
		while(fast is not None):
			if ctr%2 !=0 : 
				mid = mid.next
			fast = fast.next
			ctr+=1
		if mid:
			print(mid.data)
		else:
			print(None)

if __name__ == '__main__':
	
	llist=LinkedList()
	llist.push(1)
	llist.push(2)
	llist.push(3)
	llist.push(4)
	llist.push(5)
	llist.printList()
	llist.printMiddle()

