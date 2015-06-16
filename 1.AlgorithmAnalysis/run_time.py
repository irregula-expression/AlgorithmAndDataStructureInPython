import time
import timeit
from timeit import Timer

def sum1(n):
	start_time = time.time()
	sum = 0
	for idx in range(1, n+1):
		sum += idx
	
	end_time = time.time()
	run_time = end_time - start_time
	return sum, run_time
	

def sum2(n):
	start_time = time.time()
	sum = (n+1)*n/2
	end_time = time.time()
	run_time = end_time - start_time
	return sum, run_time

#print sum1(10000000)
#print sum2(10000000)
	
def test1():
	lst = []
	for i in range(1000):
		lst += [i]

def test2():
	lst = []
	for i in range(1000):
		lst.append(lst)
		
	
t1 = Timer("test1()", "from __main__ import test1")
print "concat: ", t1.timeit(number=10000), "milliseconds"

t2 = Timer("test2()", "from __main__ import test2")
print "append: ", t2.timeit(number = 10000), "milliseconds"