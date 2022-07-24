class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def take_input1():      # normal input
    arr = [int(i) for i in input().split()]   # last element should be -1 denoting end of array
    head = None
    for data in arr:
        if data == -1:
            break
        
        NewNode = Node(data)
        if head is None:
            head = NewNode
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
                
            curr.next = NewNode
    return head

def take_input2():      # optimised input
    arr = [int(i) for i in input().split()]   # last element should be -1 denoting end of array
    head,tail = None,None
    for data in arr:
        if data == -1:
            break
        
        NewNode = Node(data)
        if head is None:
            head = NewNode
            tail = NewNode
        else:
            tail.next = NewNode
            tail = tail.next
    return head

def printLL(head):
    while head is not None:
        print(head.data, end="->")
        head = head.next
    print("None")
        
head = take_input2()
printLL(head)
printLL(head)  # value of head is unchanged outside the printLL function