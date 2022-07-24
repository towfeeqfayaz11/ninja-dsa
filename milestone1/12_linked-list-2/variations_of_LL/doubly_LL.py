# doubly linked list
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
	
	return head

def lengthLL(head):
	count = 0
	while head:
		count+=1
		head = head.next
	return count

def insertLL(head,ele,ind):
	ln = lengthLL(head)
	if ind > ln or ind<0:                # element cannot be inserted in this case
		return head
	
	previous, curr = None, head          # previous is needed for specal case particularly (i.e; append element at end, where curr would have become None)
	newNode = Node(ele)
	for i in range(ln+1):                # +1 is for case if element need to be appended at end 
		if i == ind:
			if curr == None:             # element needs to be appended at end
				previous.next = newNode
				newNode.prev = previous
				break
			elif curr.prev is None:      # when element need to be inserted at head
				newNode.next = curr
				curr.prev = newNode
				head = newNode
				break
			else:                        # if element need to be inserted in between LL
				previous.next = newNode
				newNode.next = curr
				curr.prev = newNode
				newNode.prev = previous
				break
		previous = curr
		curr = curr.next
	
	return head

def deleteLL(head, ind):                           # delete an element from a given index
	ln = lengthLL(head)
	if ind < 0 or ind > ln-1 or ln == 0:           # if index is out of range, return original LL as it is
		return head
	
	curr = head
	for i in range(ln):
		if i == ind:
			if curr == head:        
				head = head.next
				curr.next = None
				head.prev = None
				break
			else:
				previous = curr.prev
				nxt = curr.next
				
				previous.next = nxt
				if nxt is not None:
					nxt.prev = previous
				curr.prev = None
				curr.next = None
				break
		curr = curr.next
	return head
                
		

def printLL(head):
	while head:
		print(head.data, end=' ')
		head = head.next
	print()


if __name__ == "__main__":
	head = take_input()
	printLL(head)
	head = insertLL(head,85,0)
	head = deleteLL(head, 0)
	printLL(head)
	

			
			