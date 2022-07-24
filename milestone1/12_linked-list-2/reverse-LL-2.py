class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def take_input():
    arr = [int(i) for i in input().split()]   # last element should be -1 denoting end of array
    head,tail = None,None
    for data in arr:
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

def lengthLL(head):
    count = 0
    while head is not None:
        count+=1
        head = head.next
    return count
    

# time complexity (O(n))     --> returning head as well as tail 
def reverseLL2(head):
    if head == None or head.next == None:
        return head,head
    
    smallHead, smallTail = reverseLL2(head.next)
    smallTail.next = head
    head.next = None
    
    return  smallHead, smallTail.next

head = take_input()
printLL(head)
h,t = reverseLL2(head)
printLL(h)
