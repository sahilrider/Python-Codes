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

	def printNthfromEnd(self, n):
		temp = self.head
		nthnode = None

		for i in range(n-1):
			if temp:
				temp = temp.next
		while(temp):
			if nthnode == None:
				nthnode = self.head
			else:
				nthnode = nthnode.next
			temp = temp.next

		if(nthnode):
			print(nthnode.data)
			return nthnode
		return None

if __name__ == '__main__':
	
	llist=LinkedList()

	llist.push(5)
	llist.push(6)
	llist.push(7)
	llist.push(8)
	llist.push(9)
	llist.push(10)
	llist.push(11)
	llist.printList()
	llist.printNthfromEnd(3)
