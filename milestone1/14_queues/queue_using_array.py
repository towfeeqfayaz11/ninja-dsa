class Queue:
	def __init__(self):
		self.__queue = []
		self.__length = 0
		self.__front = -1

	def enqueue(self,item):
		self.__queue.append(item)
		if self.__front == -1:
			self.__front +=1
		self.__length +=1

	def dequeue(self):
		if self.__length == 0:
			return -1
		element = self.__queue[self.__front]
		self.__front +=1
		self.__length -=1
		return element

	def front(self):
		if self.__length == 0:
			return -1
		return self.queue[self.__front]

	def size(self):
		return self.__length

	def isEmpty(self):
		return self.__length == 0


q = Queue()
print(q.dequeue())
q.enqueue(3)
q.enqueue(7)
q.enqueue(1)
q.enqueue(5)

print("size:", q.size())
while q.size():
	print(q.dequeue())
print("size:", q.size())

