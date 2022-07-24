class Stack:
	def __init__(self):
		self.__arr = []
		self.__length = 0

	def push(self,item):
		self.__arr.append(item)
		self.__length +=1

	def pop(self):
		if self.isEmpty():
			print("hey! stack is empty!!!")
			return

		self.__length -=1
		return self.__arr.pop()

	def top(self):
		if self.isEmpty():
			print("hey! stack is empty!!!")
			return

		return self.__arr[self.size() - 1]

	def size(self):
		return self.__length

	def isEmpty(self):
		return self.__length == 0




if __name__ == "__main__":
	s = Stack()

	s.push(13)
	s.push(10)
	s.push(15)

	print(s.top())

	while s.isEmpty() is False:
		print(s.pop())

	s.top()