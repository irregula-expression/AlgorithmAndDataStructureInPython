
def bubble(a_list):
	
	for i in range(len(a_list)-1, 1, -1):
		for j in range(i):
			if a_list[j] > a_list[j+1]:
				temp = a_list[j]
				a_list[j] = a_list[j+1]
				a_list[j+1] = temp
		
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble(a_list)
print a_list