from Stack import *

def to_binary_num(decimal):
	s = Stack()
	while decimal > 0:
		rem = decimal % 2
		s.push(rem)
		decimal /= 2
	ans_string = ""
	while not s.is_empty():
		ans_string += str(s.pop())
	
	return ans_string
	
print to_binary_num(233)