import Stack

def par_checker(symbol_string):
	
	s = Stack.Stack()
	idx = 0
	while idx < len(symbol_string):
		symbol = symbol_string[idx]
		if symbol == "(":
			s.push(symbol)
		if symbol == ")":
			if s.is_empty():
				return False
			else:
				s.pop()
		idx += 1
		
	return s.is_empty()

		
#print par_checker("(9+s-())")
#print par_checker(")(())")

def par_checker_general(symbol_string):
	s = Stack.Stack()
	idx = 0
	while idx < len(symbol_string):
		symbol = symbol_string[idx]
		if symbol in "([{":
			s.push(symbol)
		if symbol in ")]}":
			if s.is_empty():
				return False
			else:
				open = s.pop()
				if not matches(open, symbol):
					return False
		idx += 1
	
	return s.is_empty()
	
def matches(open, close):
	opens = "([{"
	closes = ")]}"
	return opens.index(open) == closes.index(close)
	
print par_checker_general('{{([][])}()}')
print par_checker_general('[{()]')