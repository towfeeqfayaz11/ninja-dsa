class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def take_input():
    arr = [int(i) for i in input().split()]   # last element should be -1 denoting end of array
    head,curr = None,None
    for data in arr:
        if data == -1:
            break
        
        NewNode = Node(data)
        if head is None:
            head = NewNode
            curr = NewNode
        else:
            curr.next = NewNode
            curr = curr.next
    return head

def printLL(head):
    while head is not None:
        print(head.data, end="->")
        head = head.next
    print("None")

def lengthLL(head):
    count = 0
    while head is not None:
        count+=1
        head = head.next
    return count

def insertAt(head,ele,i):
    if i < 0 or i>lengthLL(head):
        return head
    
    newNode = Node(ele)
    prev,curr = None,head
    count = 0
    while count < i:
        prev = curr
        curr = curr.next
        count+=1
    if prev is None:
        newNode.next = head
        head = newNode
    else:
        prev.next = newNode
        newNode.next = curr
    
    return head
    
    

    

head = take_input()
printLL(head)
printLL(head)  # value of head is unchanged outside the printLL function
new_head = insertAt(head,12,3)
printLL(new_head)
