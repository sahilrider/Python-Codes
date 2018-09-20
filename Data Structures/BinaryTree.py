'''
This file contains all tree traversal and level wise insertion in tree
'''

import queue
'''class for node of binary tree'''
class Node(object):
	"""docstring for Node"""
	def __init__(self, val=None):
		super(Node, self).__init__()
		self.left = None
		self.right = None
		self.val = val
		
'''class for binary tree'''
class BinaryTree(object):
	"""docstring for BinaryTree"""
	def __init__(self):
		super(BinaryTree, self).__init__()
		self.root = None

	'''Insert node level wise'''
	def insert(self, val):

		new_node = Node(val)
		if self.root is None:
			self.root = new_node
			return

		Q = queue.Queue(maxsize=20)
		Q.put(self.root)	#Enqueue
		while(Q.empty() is not True):
			temp = Q.get()	#Dequeue
			if temp.left:
				Q.put(temp.left)
			else:
				temp.left = new_node
				Q.queue.clear()
				return

			if temp.right:
				Q.put(temp.right)
			else:
				temp.right = new_node
				Q.queue.clear()
				return
		Q.queue.clear()

	'''Inorder Traversal'''
	def inorder(self,root):
		res = []
		if root:
			res = self.inorder(root.left)
			res.append(root.val)
			res = res + self.inorder(root.right)
		return res

	'''Preorder Traversal'''
	def preorder(self,root):
		res = []
		if root:
			res.append(root.val)
			res = res + self.preorder(root.left)
			res = res + self.preorder(root.right)
		return res

	'''Postorder Traversal'''
	def postorder(self,root):
		res = []
		if root:
			res = self.postorder(root.left)
			res = res + self.postorder(root.right)
			res.append(root.val)
		return res

	'''Level Order Traversal'''
	def levelorder(self,root):
		res = []
		if root is None:
			return res

		Q = queue.Queue(maxsize=20)
		Q.put(root)
		while(Q.empty() is not True):
			#print(list(Q.queue),res)
			temp = Q.get()
			res.append(temp.val)
			if temp.left:
				Q.put(temp.left)
			if temp.right:
				Q.put(temp.right)
		Q.queue.clear()
		return res

if __name__ == '__main__':
	btree = BinaryTree()

	btree.root = Node(1)
	btree.root.left =Node(2)
	btree.root.right = Node(3)
	btree.insert(4)
	btree.insert(5)
	btree.insert(6)
	print(btree.preorder(btree.root))
	print(btree.inorder(btree.root))
	print(btree.postorder(btree.root))
	print(btree.levelorder(btree.root))