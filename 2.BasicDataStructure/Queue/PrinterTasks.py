import random
from Queue import *

class Printer:
	def __init__(self, ppm):
		self._current_task = None
		self._time_remaining = 0
		self._rate = ppm
		
	def busy(self):
		if self._current_task == None:
			return False
		else:
			return True
	def start_new(self, new_task):
		self._current_task = new_task
		self._time_remaining = new_task.get_num_pages() * 60.0 / self._rate
		
	def tick(self):
		if self._current_task != None:
			self._time_remaining -= 1
			if self._time_remaining <= 0:
				self._current_task = None
		
		
class Task:
	def __init__(self, start_time):
		self._pages = random.randrange(1, 21)
		self._start_time = start_time
		
	def get_num_pages(self):
		return self._pages
		
	def wait_time(self, current_time):
		return current_time - self._start_time

		

def simulation(total_seconds, page_per_minute):
	
	lab_printer = Printer(page_per_minute)
	tasks_queue = Queue()
	wait_times = []
	
	for second in range(total_seconds):
		if new_print_task():
			new_task = Task(second)
			tasks_queue.enqueue(new_task)
		
		if (not lab_printer.busy()) and (not tasks_queue.is_empty()):
			next_task = tasks_queue.dequeue()
			wait_times.append(next_task.wait_time(second))
			lab_printer.start_new(next_task)
			
		lab_printer.tick()
		
	average_time = float(sum(wait_times)) / len(wait_times)
	
	print "Average wait time is: %6.2f, %3d tasks remaining" %(average_time, tasks_queue.size())

	
def new_print_task():
	if random.randrange(1, 181) == 180:
		return True	
	else:
		return False

for i in range(10):
	simulation(3600, 10)