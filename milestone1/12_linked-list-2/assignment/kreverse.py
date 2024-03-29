# kReverse

# Given a singly linked list of integers, reverse the nodes of the linked list 'k' at a time and return its modified list.
#  'k' is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a 
#  multiple of 'k,' then left-out nodes, in the end, should be reversed as well.

# Example :
# Given this linked list: 1 -> 2 -> 3 -> 4 -> 5

# For k = 2, you should return: 2 -> 1 -> 4 -> 3 -> 5

# For k = 3, you should return: 3 -> 2 -> 1 -> 5 -> 4
#  Note :
# No need to print the list, it has already been taken care. Only return the new head to the list.
#  Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# The first line of each test case or query contains the elements of the singly linked list separated by a single space.

# The second line of input contains a single integer depicting the value of 'k'.
#  Remember/Consider :
# While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
# Output format :
# For each test case/query, print the elements of the updated singly linked list.

# Output for every test case will be printed in a separate line.
# Constraints :
# 1 <= t <= 10^2
# 0 <= M <= 10^5
# Where M is the size of the singly linked list.
# 0 <= k <= M

# Time Limit:  1sec
# Sample Input 1 :
# 1
# 1 2 3 4 5 6 7 8 9 10 -1
# 4
# Sample Output 1 :
# 4 3 2 1 8 7 6 5 10 9
# Sample Input 2 :
# 2
# 1 2 3 4 5 -1
# 0
# 10 20 30 40 -1
# 4
# Sample Output 2 :
# 1 2 3 4 5 
# 40 30 20 10


###########################################################################################


# solution 1:
from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

# reverse linkedlist and return head, tail for the reversed linkedlist
def reverseLinkedListRec(head):
    if head is None or head.next is None:
        return head,head
    smallHead,smallTail=reverseLinkedListRec(head.next)
    head.next.next=head
    head.next=None
    return smallHead, head

def kReverse(head, k) :
    if head is None or head.next is None or k <= 1:
        return head 
    
    curr,tail = head,head
    count = 1
    while count < k and tail.next:
        tail = tail.next
        count+=1
    
    head = tail.next
    tail.next = None
    rhead,rtail = reverseLinkedListRec(curr)
    rtail.next = kReverse(head, k)
    
    return rhead
    



#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head




def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    k = int(stdin.readline().strip())

    newHead = kReverse(head, k)
    printLinkedList(newHead)

    t -= 1



#################################################################################

# solution2:
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def reverse(head):
    curr = head
    prev = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    tail = head
    head = prev
    return head, tail

def LengthLL(head):
    length = 0
    while head is not None:
        head = head.next
        length += 1
    return length

def kReverse(head, k) :
	#Your code goes here
    if k<0:
        return
    if head is None or head.next is None or k==0:
        return head
    if k>LengthLL(head):
        head, tail = reverse(head)
        return head
    curr = head
    j=1
    while curr is not None and j<k:
        curr = curr.next
        j+=1
    newhead = curr.next
    smallhead = kReverse(newhead, k)
    curr.next = None
    mainhead, maintail = reverse(head)
    
    maintail.next = smallhead
    return mainhead
    



#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head




def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    k = int(stdin.readline().strip())

    newHead = kReverse(head, k)
    printLinkedList(newHead)

    t -= 1

