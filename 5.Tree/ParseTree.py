from BinaryTree import BinaryTree
from Stack import *

def buildParseTree(exp_string):
	exp_list = exp_string.split()
	parent_stack = Stack()
	root = BinaryTree(None)
	current_node = root
	
	for token in exp_list:
		if token == "(":
			current_node.insertLeft(None)
			parent_stack.push(current_node)
			current_node = current_node.getLeftChild()
		
		elif token in "+-*/":
			current_node.setRootVal(token)
			parent_stack.push(current_node)
			current_node.insertRight(None)
			current_node = current_node.getRightChild()
			
		elif token == ")":
			if parent_stack.size() > 0:
				parent_node = parent_stack.pop()
				current_node = parent_node
		
		else:
			current_node.setRootVal(float(token))
			if parent_stack.size() > 0:
				parent_node = parent_stack.pop()
				current_node = parent_node
	
	return root
	
#pt = buildParseTree("( ( 10 + 5 ) * ( 3 - 9 ) )")

def evaluate(parseTree):
	token = parseTree.getRootVal()
	leftChild = parseTree.getLeftChild()
	rightChild = parseTree.getRightChild()
	
	if leftChild != None and rightChild != None:
		if token == "+":
			return evaluate(leftChild) + evaluate(rightChild)
		elif token == "-":
			return evaluate(leftChild) - evaluate(rightChild)
		elif token == "*":
			return evaluate(leftChild) * evaluate(rightChild)
		else:
			return evaluate(leftChild) / evaluate(rightChild)
			
	else:
		return token
		
#print evaluate(pt)