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

	def isCycle(self):

		slowptr = self.head
		fastptr = self.head

		while(slowptr and fastptr and fastptr.next):
			fastptr = fastptr.next.next
			slowptr = slowptr.next
			if slowptr == fastptr :
				return 1
		return 0

if __name__ == '__main__':
	
	llist=LinkedList()
	llist.push(1)
	llist.push(2)
	llist.push(3)
	llist.push(4)
	print(llist.isCycle())

	'''After adding Cycle'''
	llist.head.next.next.next = llist.head
	print(llist.isCycle())

