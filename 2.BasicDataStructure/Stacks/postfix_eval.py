from Stack import *
from infix_to_postfix import *

def postfix_eval(postfix_expr):
	token_list = postfix_expr.split()
	operand_stack = Stack()
	
	for token in token_list:
		if token in "0123456789":
			operand_stack.push(int(token))
		else:
			operand1 = operand_stack.pop()
			operand2 = operand_stack.pop()
			result = do_math(operand1, operand2, token)
			operand_stack.push(result)
	
	return operand_stack.pop()

def do_math(opd1, opd2, op):
	if op == "+":
		return opd1 + opd2
	elif op == "-":
		return opd1 - opd2
	elif op =="*":
		return opd1 * opd2
	else:
		return opd1 / opd2

print postfix_eval(infix_to_postfix("( 1 + 2 ) * ( 3 + 4 ) "))
print postfix_eval(infix_to_postfix("1 + 2 * 3 + 4"))