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

	def reverseList_iteration(self):

		prev = None
		nextNode = None
		curr = self.head
		while curr:
			nextNode = curr.next
			curr.next = prev
			prev = curr
			curr = nextNode
		self.head = prev

	def reverseList_recursion(self, curr, prev):

		if(self.head == None):
			return None
		if(curr.next == None):
			self.head = curr
			curr.next = prev
			return

		next = curr.next
		curr.next = prev
		self.reverseList_recursion(next,curr)




if __name__ == '__main__':
	
	llist=LinkedList()
	llist.push(1)
	llist.push(2)
	llist.push(3)
	llist.push(4)
	llist.printList()

	llist.reverseList_iteration()
	llist.printList()

	llist.reverseList_recursion(llist.head, None)
	llist.printList()
	

