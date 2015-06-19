from Deque import *

def palindrome_checker(a_string):
	
	char_deque = Deque()
	
	for char in a_string:
		char_deque.add_rear(char)
		
	while char_deque.size() > 1:
		first = char_deque.remove_front()
		last = char_deque.remove_rear()
		if first != last:
			return False
	
	return True
	

	
print(palindrome_checker("lsdkjfskf"))
print(palindrome_checker("radar"))