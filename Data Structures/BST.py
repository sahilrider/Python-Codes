import queue
class Node(object):
	"""docstring for Node"""
	def __init__(self, data=None):
		super(Node, self).__init__()
		self.data = data
		self.left = None
		self.right = None

class BST(object):
	"""docstring for BST"""
	def __init__(self):
		super(BST, self).__init__()
		self.root = None

	'''Inorder Traversal'''
	def inorder(self,root):
		res = []
		if root:
			res = self.inorder(root.left)
			res.append(root.data)
			res = res + self.inorder(root.right)
		return res

	'''Finding an element in BST'''
	def find(self, data):
		if self.root is None:
			return 0
		curr = self.root
		while curr:
			if data == curr.data:
				return 1
			elif data < curr.data:
				curr = curr.left
			else:
				curr = curr.right
		return 0

	'''Finding min element in BST'''
	def findMin(self, root):
		if root is None:
			return 0
		root = self.root
		while root.left is not None:
			root = root.left
		return root.data

	'''Finding max element in BST'''
	def findMax(self, root):
		if root == None:
			return 0
		while root.right is not None:
			root = root.right
		return root.data

	'''Inserting an element in BST'''
	def insert(self, root, data):
		if root == None:
			root = Node(data)
		else:
			if data < root.data:
				root.left = self.insert(root.left, data)
			else:
				root.right = self.insert(root.right, data)
		return root

	'''Deleting an element in BST'''
	def delete(self, root, data):
		if root == None:
			return None
		elif data < root.data:
			root.left = self.delete(root.left, data)
		elif data > root.data:
			root.right = self.delete(root.right, data)
		else:
			#Node has two children
			if (root.left is not None) and (root.right is not None):
				temp = self.findMax(root.left)
				root.data = temp
				root.left = self.delete(root.left, root.data)
			else:
				if root.left:	#only left child
					root = root.left
				elif root.right:	#only right child
					root = root.right
				else:	#no child
					root = None
		return root


if __name__ == '__main__':
	bst =BST()
	bst.root = bst.insert(bst.root, 5)
	bst.root = bst.insert(bst.root, 4)
	bst.root = bst.insert(bst.root, 8)
	bst.root = bst.insert(bst.root, 1)
	print(bst.find(9))
	print(bst.findMin(bst.root))
	print(bst.findMax(bst.root))

	bst.delete(bst.root, 5)

	print(bst.inorder(bst.root))


		
		