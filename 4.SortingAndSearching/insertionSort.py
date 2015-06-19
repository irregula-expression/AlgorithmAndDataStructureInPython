
def insertion_sort(a_list):
	
	for idx in range(1, len(a_list)):
		current_value = a_list[idx]
		pos = idx -1
		while a_list[pos] > current_value and pos >= 0:
			a_list[pos+1] = a_list[pos]
			pos -= 1
			
		a_list[pos+1] = current_value		
		
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(a_list)
print a_list