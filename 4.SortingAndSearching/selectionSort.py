
def selection_sort(a_list):
	
	for i in range(len(a_list)-1, 0, -1):
		max_pos = 0
		for j in range(1, i+1):
			if a_list[max_pos] < a_list[j]:
				max_pos = j
		
		temp = a_list[max_pos]
		a_list[max_pos] = a_list[i]
		a_list[i] = temp
		
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(a_list)
print a_list