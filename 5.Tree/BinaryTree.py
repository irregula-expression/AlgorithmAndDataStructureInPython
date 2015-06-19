
class BinaryTree:
	
	def __init__(self, root_value):
		self._key = root_value
		self._left = None
		self._right = None
		
	def insertLeft(self, new_value):
		if self._left == None:
			self._left = BinaryTree(new_value)
		else:
			t = BinaryTree(new_value)
			t._left = self._left
			self._left = t
			
	def insertRight(self, new_value):
		if self._right == None:
			self._right = BinaryTree(new_value)
		else:
			t = BinaryTree(new_value)
			t._right = self._right
			self._right = t
			
	def getRightChild(self):
		return self._right
		
	def getLeftChild(self):
		return self._left
		
	def setRootVal(self, new_root_value):
		self._key = new_root_value
		
	def getRootVal(self):
		return self._key
		
	def preorder(self):
		print self._key
		if self._left != None:
			self._left.preorder()
		if self._right != None:
			self._right.preorder()
#testTree = BinaryTree("a")
#testTree.insertLeft("b")
#testTree.insertRight("c")
#testTree.getLeftChild().insertRight("d")
#testTree.getRightChild().insertLeft("e")
#testTree.getRightChild().insertRight("f")

#print testTree.getRightChild().getRootVal() == 'c'
#print testTree.getLeftChild().getRightChild().getRootVal() == 'd'
#print testTree.getRightChild().getLeftChild().getRootVal() == 'e'

			
