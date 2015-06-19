
def toString(n, base):
	convert_string = "0123456789ABCDEF"
	
	if n < base:
		return convert_string[n]
	else:
		return toString(n/base, base) + convert_string[n%base]
		
print toString(1453, 16)

