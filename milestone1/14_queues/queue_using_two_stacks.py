# queue using two stack
# has two variations
# enqueue()          O(1)     O(n)
# deqeue()           O(n)     O(1)
# front()            O(1)     O(1)
# size()             O(1)     O(1)
# isEmpty()          O(1)     O(1) 


# enqueue = O(1), dequeue = O(n)
class Queue1:
	def __init__(self):
		# initializing two stacks
		self.__s1 = []
		self.__s2 = []
	
	def enqueue(self,data):
		self.__s1.append(data)
	
	def dequeue(self):
		if len(self.__s1) == 0:
			return "Queue is empty!!!"
		
		while len(self.__s1) != 1:
			self.__s2.append(self.__s1.pop())
		
		tmp = self.__s1.pop()
		
		while len(self.__s2) != 0:
			self.__s1.append(self.__s2.pop())
		
		return tmp
	
	def front(self):
		if len(self.__s1) == 0:
			return "Queue is empty!!!"
			
		return self.__s1[0]
	
	def size(self):
		return len(self.__s1)
	
	def isEmpty(self):
		return len(self.__s1) == 0
		
			
		
	
	
	


# enqueue = O(n), dequeue = O(1)
class Queue2:
	def __init__(self):
		# initializing two stacks
		self.__s1 = []
		self.__s2 = []
	
	def enqueue(self,data):
		while len(self.__s1) != 0:
			self.__s2.append(self.__s1.pop())
			
		self.__s1.append(data)
		
		while len(self.__s2) != 0:
			self.__s1.append(self.__s2.pop())
	
	def dequeue(self):
		if len(self.__s1) == 0:
			return "Queue is empty!!!"
		
		return self.__s1.pop()
	
	def front(self):
		if len(self.__s1) == 0:
			return "Queue is empty!!!"
			
		return self.__s1[-1]
	
	def size(self):
		return len(self.__s1)
	
	def isEmpty(self):
		return len(self.__s1) == 0
		
		


if __name__ == "__main__":
	q1 = Queue1()
	print(q1.isEmpty())
	print(q1.size())
	print(q1.dequeue())
	q1.enqueue(3)
	q1.enqueue(5)
	q1.enqueue(7)
	q1.enqueue(9)
	print(q1.isEmpty())
	print(q1.size())
	
	while not q1.isEmpty():
		print(q1.dequeue())
	
	print(q1.isEmpty())
	print(q1.size())
	
	print("--------------")
	q2 = Queue2()
	print(q2.isEmpty())
	print(q2.size())
	print(q2.dequeue())
	q2.enqueue(7)
	q2.enqueue(11)
	q2.enqueue(0)
	q2.enqueue(9)
	print(q2.isEmpty())
	print(q2.size())
	
	while not q2.isEmpty():
		print(q2.dequeue())
	
	print(q2.isEmpty())
	print(q2.size())