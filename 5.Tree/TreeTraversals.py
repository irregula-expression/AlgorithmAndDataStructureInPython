from BinaryTree import BinaryTree
from ParseTree import *

def preorder(tree):
	if tree:
		print tree.getRootVal()
		preorder(tree.getLeftChild())
		preorder(tree.getRightChild())
		
def inorder(tree):
	if tree:
		inorder(tree.getLeftChild())
		print tree.getRootVal()
		inorder(tree.getRightChild())

		
def postorder(tree):
	if tree:
		postorder(tree.getLeftChild())
		postorder(tree.getRightChild())
		print tree.getRootVal()
		
def printexp(parseTree):
	ans = ""
	if parseTree:
		ans = "( " + printexp(parseTree.getLeftChild())
		ans += str(parseTree.getRootVal())
		ans += printexp(parseTree.getRightChild()) + " )"
		
	return ans
	
pt = buildParseTree("( ( 10 + 5 ) * ( 3 - 9 ) )")
print printexp(pt)
#preorder(pt)
#pt.preorder()
#inorder(pt)

#testTree = BinaryTree("a")
#testTree.insertLeft("b")
#testTree.insertRight("c")
#inorder(testTree)


