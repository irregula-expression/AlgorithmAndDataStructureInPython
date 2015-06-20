
class TreeNode:
	
	def __init__(self, key, val, left=None, right=None, parent=None):
		self._key = key
		self._val = val
		self._leftChild = left
		self._rightChild = right
		self._parent = parent
		
	def hasLeftChild(self):
		return self._leftChild != None
		
	def hasRightChild(self):
		return self._rightChild != None
		
	def isLeftChild(self):
		return self._parent != None and self._parent._leftChild == self
		
	def isRightChild(self):
		return self._parent != None and self._parent._rightChild == self
		
	def isRoot(self):
		return self._parent == None
		
	def isLeaf(self):
		return self._leftChild == None and self._rightChild == None
	
	def hasAnyChildren(self):
		return self._leftChild != None or self._rightChild != None
		
	def hasBothChildren(self):
		return self._leftChild != None and self._rightChild != None
		
	def setNodeData(self, key, value, lc, rc):
		self._key = key
		self._val = value
		self._leftChild = lc
		self._rightChild = rc
		if self.hasLeftChild():
			self._leftChild.parent = self
		if self.hasRightChild():
			self._rightChild.parent = self
			

			
class BinarySearchTree:
	
	def __init__(self):
		self._root = None
		self._size = 0
		
	def length(self):
		return self._size
		
	def __len__(self):
		return self._size
		
	def __iter__(self):
		return self.root.__iter__()
		
	def put(self, key, val):
		if self._root == None:
			sefl._root = TreeNode(key, val)
		else:
			self._put(key, val, self._root)
		
		self._size += 1
		
	def _put(self, key, val, currentNode):
		if key < currentNode._key:
			if currentNode.hasLeftChild():
				self._put(key, val, currentNode._leftChild)
			else:
				currentNode._leftChild = TreeNode(key, val, parent=currentNode)
				
		elif key > currentNode._key:
			if currentNode.hasRightChild():
				self._put(key, val, currentNode._rightChild)
			else:
				currentNode._rightChild = TreeNode(key, val, parent=currentNode)
		
		else:
			currentNode._val = val
	
	def __setitem__(self, key, val):
		self.put(key, val)
		
	def get(self, key):
		theNode = self._get(key, self._root)
		if theNode != None:
			return theNode._val
		else:
			return None
		
	def _get(self, key, currentNode):
		if currentNode == None:
			return None
		elif currentNode._key == key:
			return currentNode
		elif key < currentNode._key:
			self._get(key, currentNode._leftChild)
		else:
			self._get(key, currentNode._rightChild)
			
	def __contain__(self, key):
		if self._get(key, self._root):
			return True
		else:
			return False
			
	
		
		
		
		
		
		
		
		
		
		