
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
	
	def findSuccessor(self):
		succ = None
		if self.hasRightChild():
			succ = self.rightChild.findMin()
		else:
			if self._parent != None:
				if self.isLeftChild():
					succ = self._parent
				else:
					self._parent._rightChild = None
					succ = self._parent.findSuccessor()
					self._parent._rightChild = self
		return succ
		
	def finMin(self):
		currentNode = self
		while currentNode.hasLeftChild():
			currentNode = currentNode._leftChild
		return currentNode
		
	def splicOut(self):
		if self.isLeaf():
			if self.isLeftChild():
				self._parent._leftChild = None
			else:
				self._parent._rightChild = None
				
		elif self.hasAnyChildren():
			if self.hasLeftChild():
				if self.isLeftChild():
					self._parent._leftChild = self._leftChild
				else:
					self._parent._rightChild = self._leftChild
				self._leftChild.parent = self._parent
			else:
				if self.isLeftChild():
					self._parent._leftChild = self._rightChild
				else:
					self._parent._rightChild =self._rightChild
				self._rightChild._parent = self._parent
	
	def __iter__(self):
		if self != None:
			if self.hasLeftChild():
				for elem in self._leftChild:
					yield elem
			
			yield self._key
			
			if self.hasRightChild():
				for elem in self._rightChild:
					yield elem
						
			

			
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
			
	def delete(self, key):
		if self._size == 1 and self._root._key == key:
			self._root = None
			self._size -= 1
		
		elif self._size > 1:
			nodeToRemove = self._get(key, self._root)
			if nodeToRemove != None:
				self.remove(nodeToRemove)
			else:
				raise KeyError("error, key not in tree")
				
		else:
			raise KeyError("error, key not in tree")
			
	def remove(self, currentNode):
		if currentNode.isLeaf():
			if currentNode.isLeftChild():
				currentNode._parent._leftChild = None
			else:
				currentNode._parent._rightChild = None
				
		elif currentNode.hasBothChildren():
			succ = currentNode.findSuccessor()
			succ.spliceOut()
			currentNode._key = succ._key
			currentNode._val = succ._val
			
		else:
			if currentNode.hasLeftChild():
				if currentNode.isLeftChild():
					currentNode._parent._leftChild = currentNode._leftChild
					currentNode._leftChild._parent = currentNode._parent
				elif currentNode.isRightChild():
					currentNode._parent._rightChild = currentNode._leftChild
					currentNode._leftChild._parent = currentNode._parent
				else:
					currentNode.setNodeData(self._leftChild._key, self._leftChild._val,
											self._leftChild._leftChild, self._leftChild._rightChild)
				
			else: #has right child
				if currentNode.isLeftChild():
					currentNode._parent._leftChild = currentNode._rightChild
					currentNode._rightChild._parent = currentNode._parent
				elif currentNode.isRightChild():
					currentNode._parent._rightChild = currentNode._rightChild
					currentNode._rightChild._parent = currentNode._parent
				else:
					currentNode.setNodeData(self._rightChild._key, self._rightChild._val,
											self._rightChild._leftChild, self._rightChild._rightChild)

