from BinarySearchTree import *

class AVLTree(BinarySearchTree):
	def __init__(self):
		BinarySearchTree.__init__(self)
		
	def _put(self, key, val, currentNode):
		if key < currentNode._key:
			if currentNode.hasLeftChild():
				self._put(key, val, currentNode._leftChild)
			else:
				currentNode._leftChild = TreeNode(key, val, parent=currentNode)
				self.updateBalance(currentNode._leftChild)
				
		elif key > currentNode._key:
			if currentNode.hasRightChild():
				self._put(key, val, currentNode._rightChild)
			else:
				currentNode._rightChild = TreeNode(key, val, parent=currentNode)
				self.updateBalance(currentNode._rightChild)
			