from Stack import *

def infix_to_postfix(infix_expr):
	
	token_list = infix_expr.split()
	op_stack = Stack()
	postfix_list = []
	prec = {"*":3, "/":3, "+":2, "-":2, "(":1}
	
	for token in token_list:
		if token in "0123456789" or token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			postfix_list.append(token)
		
		elif token == "(":
			op_stack.push(token)
		elif token == ")":
			top_token = op_stack.pop()
			while top_token != "(":
				postfix_list.append(top_token)
				top_token = op_stack.pop()
		else:
			while (not op_stack.is_empty()) and prec[op_stack.peek()] >= prec[token]:
				postfix_list.append(op_stack.pop())
			op_stack.push(token)
	
	while (not op_stack.is_empty()):
		postfix_list.append(op_stack.pop())
	
	return " ".join(postfix_list)

#print infix_to_postfix("A + B + C + D")
#print infix_to_postfix("( A + B ) * ( C + D ) ")
#print infix_to_postfix("A + B * C + D")