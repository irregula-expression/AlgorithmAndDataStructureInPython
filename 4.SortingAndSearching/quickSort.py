
def quick_sort_helper(a_list, first, last):
	if first < last:
		split_point = partition(a_list, first, last)
		quick_sort_helper(a_list, first, split_point-1)
		quick_sort_helper(a_list, split_point+1, last)
	
		

def partition(a_list, first, last):
	pivot = a_list[first]
	leftmark = first + 1
	rightmark = last
	done = False
	
	while not done:
		while rightmark >= leftmark and a_list[leftmark] <= pivot:
			leftmark += 1
		while rightmark >= leftmark and a_list[rightmark] >= pivot:
			rightmark -= 1
		
		if rightmark < leftmark:
			done = True
		else:
			temp = a_list[leftmark]
			a_list[leftmark] = a_list[rightmark]
			a_list[rightmark] = temp
	
	a_list[first] = a_list[rightmark]
	a_list[rightmark] = pivot
		
	#print rightmark
	return rightmark
		
	
	
def quick_sort(a_list):
	quick_sort_helper(a_list, 0, len(a_list)-1)
	
	
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(a_list)
print a_list