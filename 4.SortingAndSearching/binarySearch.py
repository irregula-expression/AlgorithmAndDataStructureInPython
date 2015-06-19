
def binary_search(a_sorted_list, item):
	if len(a_sorted_list) == 0:
		return False
	
	mid = len(a_sorted_list) / 2
	if a_sorted_list[mid] == item:
		return True
	elif a_sorted_list[mid] > item:
		return binary_search(a_sorted_list[:mid], item)
	else:
		return binary_search(a_sorted_list[mid+1:], item)

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print binary_search(test_list, 3)
print binary_search(test_list, 13)