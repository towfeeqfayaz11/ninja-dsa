# doubly circular linked list
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None


def take_input():
	arr = [int(i) for i in input().split()]
	
	head = None
	tail = None
	for ele in arr:
		newNode = Node(ele)
		if head == None:
			head = newNode
			tail = newNode
		else:
			newNode.prev = tail
			tail.next = newNode
			tail = tail.next
	tail.next = head               # modification for circular variation
	head.prev = tail               # modificaton for circular variation
	return head

def lengthLL(head):
	count = 0
	if head == None:
		return count
		
	curr = head
	while True:
		count+=1
		curr = curr.next
		if curr == head:
			break
	return count

def insertLL(head,ele,ind):
	ln = lengthLL(head)
	if ind > ln or ind<0:                # element cannot be inserted in this case
		return head
	
	curr = head     # previous is needed for specal case particularly (i.e; append element at end, where curr would have become None)
	newNode = Node(ele)
	i = 0
	while i < ind:
		i+=1
		curr = curr.next
		
	previous = curr.prev
	previous.next = newNode
	newNode.next = curr
	curr.prev = newNode
	newNode.prev = previous
	if curr == head and i == 0:
		head = newNode
	
	return head

def deleteLL(head, ind):                       # delete an element from a given index
	ln = lengthLL(head)
	if ind < 0 or ind > ln-1 or ln == 0:       # if index is out of range, return original LL as it is
		return head
	
	curr = head
	i = 0
	while i<ind:
		i+=1
		curr = curr.next
	
	previous = curr.prev
	nxt = curr.next
	
	previous.next = nxt
	nxt.prev = previous
	if curr == head:
		head = head.next
	
	return head
                
		

def printLL(head):
	curr = head
	while True:
		print(curr.data, end=' ')
		curr = curr.next
		if curr == head:
			break
	print()


if __name__ == "__main__":
	head = take_input()
	printLL(head)
	print(lengthLL(head))
	head = insertLL(head,14,0)
	printLL(head)
	head = deleteLL(head, 0)
	printLL(head)