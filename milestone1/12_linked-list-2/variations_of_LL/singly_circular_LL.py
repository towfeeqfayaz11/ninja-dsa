# circular singly linked list
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def take_input():
	arr = [int(i) for i in input().split()]
	head,tail = None,None
	
	for ele in arr:
		newNode = Node(ele)
		if head == None:
			head = newNode
			tail = newNode
		else:
			tail.next = newNode
			tail = tail.next
	
	tail.next = head                 # variation for circular LL
	return head
	
def printLL(head):
	if head == None:
		print("Empty LL !!!")
		return
	curr = head
	while True:
		print(curr.data, end=" ")
		curr = curr.next
		if curr == head:
			break
	print()
		
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
def get_head_tail(head):
	curr = head
	while curr.next != head:
		curr = curr.next
	
	return curr, head
		
def insertLL(head,ele,ind):
	ln = lengthLL(head)
	if ind > ln or ind < 0 or (ln == 0 and ind != 0):
		return head
	
	# get prev for curr head
	prev, curr = get_head_tail(head)
	
	newNode = Node(ele)
	i = 0
	while i < ind:
		prev = curr
		curr = curr.next
		i+=1
	
	prev.next = newNode
	newNode.next = curr
	if curr == head and i == 0:
		head = newNode
	
	return head
	
def deleteLL(head,ind):
	ln = lengthLL(head)
	if ind == 0 and ln == 1:       # if LL has a single element and needs to be deleted
		return None
	if head == None or ind < 0 or ind > ln -1:
		return head
	prev, curr = get_head_tail(head)
	i = 0
	while i < ind:
		prev = curr
		curr = curr.next
		i+=1
	
	prev.next = curr.next
	if curr == head:
		head = head.next
	
	return head
	
if __name__ == "__main__":
	head = take_input()
	printLL(head)
	print(lengthLL(head))
	head = insertLL(head,51,0)
	printLL(head)
	print("after deletion")
	new_head = deleteLL(head,0)
	printLL(new_head)