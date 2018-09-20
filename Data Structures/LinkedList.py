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

	"""Inserting node after any certain node"""
	def insertAfter(self, prev_node, data):

		if prev_node is None :
			print("Invalid Node")
			return

		new_node = Node(data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	"""Inserting new node at the end"""
	def append(self,data):

		new_node = Node(data)

		if self.head == None:
			self.head = new_node
		else:
			tail = self.head
			while tail.next !=None:
				tail = tail.next
			tail.next = new_node

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

	"""Delete list"""
	def deleteList(self):

		if self.head == None :
			print("List is already empty!!!")
			return

		current = self.head
		self.head = None
		while current:
			nxt = current.next
			del current.data
			del current.next
			current = nxt

	"""Delete a node by key"""
	def delKey(self,key):

		if self.head == None:
			print("List is already empty!!!")
			return

		temp = self.head

		# if head node needs to be deleted
		if temp.data == key:
			self.head = self.head.next
			temp = None
			return


		while temp:
			if temp.data == key :
				break
			prev=temp
			temp=temp.next

		if temp == None:
			print("Key is not present")
			return

		prev.next=temp.next
		temp = None
			
	""" Delete a node by position starting with 0 """
	def delPos(self, pos):

		if self.head == None :
			print("List is already empty")
			return 

		temp = self.head

		#if head is to be deleted
		if pos == 0:
			self.head = self.head.next
			temp = None
			return 

		#go till pos-1
		for i in range(pos-1):
			temp = temp.next
			if temp is None:
				break

		#if there is no element at "pos" position
		if (temp is None) or (temp.next is None):
			return

		to_be_del=temp.next
		temp.next=temp.next.next
		to_be_del = None

			 


if __name__ == '__main__':
	
	llist=LinkedList()

	llist.push(5)
	llist.printList()

	llist.push(2)
	llist.printList()

	llist.insertAfter(llist.head.next,7)
	llist.printList()

	llist.append(8)
	llist.printList()

	llist.delKey(2)
	llist.printList()

	llist.delPos(1)
	llist.printList()

	llist.deleteList()
	llist.printList()
