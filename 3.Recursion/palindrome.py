
def palindrome(a_string):
	if len(a_string) <= 1:
		return True
	return (a_string[0] == a_string[len(a_string)-1]) and \
            palindrome(a_string[1:len(a_string)-1])
			
print palindrome("kayak")