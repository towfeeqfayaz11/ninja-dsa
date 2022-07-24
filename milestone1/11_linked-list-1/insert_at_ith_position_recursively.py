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

def insert_Recursive(head, ele, i): # insert recursively
    if i < 0:
        return head
    if i == 0:
        newNode = Node(ele)
        newNode.next = head
        return newNode
    if head is None:
        return head
    smallHead = insert_Rec(head.next, ele, i-1)
    head.next = smallHead
    return head
    
    

    

head = take_input()
printLL(head)  # value of head is unchanged outside the printLL function
printLL(new_head)
head = insert_Recursive(new_head,17,5)
printLL(head)
