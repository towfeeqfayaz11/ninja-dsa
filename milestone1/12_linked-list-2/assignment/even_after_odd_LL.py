# Even after Odd LinkedList

# For a given singly linked list of integers, arrange the elements such that all the even numbers are placed after the odd numbers. 
# The relative order of the odd and even terms should remain unchanged.
# Note :
# No need to print the list, it has already been taken care. Only return the new head to the list.
# Input format:
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# The first line of each test case or query contains the elements of the singly linked list separated by a single space. 
#  Remember/Consider :
# While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
# Output format:
# For each test case/query, print the elements of the updated singly linked list.

# Output for every test case will be printed in a seperate line.
# Constraints :
# 1 <= t <= 10^2
# 0 <= M <= 10^5
# Where M is the size of the singly linked list.

# Time Limit: 1sec
# Sample Input 1 :
# 1
# 1 4 5 2 -1
# Sample Output 1 :
# 1 5 4 2 
# Sample Input 2 :
# 2
# 1 11 3 6 8 0 9 -1
# 10 20 30 40 -1
# Sample Output 2 :
# 1 11 3 9 6 8 0
# 10 20 30 40

#################################################################################################

# solution 1:
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def evenAfterOdd(head) :
    #Your code goes here
    h1,t1 = None, None  # will point to odd linkedlist
    h2,t2 = None, None  # will point to even linkedlist
    
    while head:
        if head.data % 2 != 0:
            if h1 is None:
                h1,t1 = head,head
                head = head.next
            else:
                t1.next = head
                head = head.next
                t1 = t1.next
        else:
            if h2 is None:
                h2,t2 = head,head
                head = head.next
            else:
                t2.next = head
                head = head.next
                t2 = t2.next
        
    if h1 is None:     # if all elements are even in LL
        return h2
    if h2 is None:     # if all elements are odd in 
        return h1
    
    t1.next = h2
    t2.next = None
    
    return h1
        
        


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


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    newHead = evenAfterOdd(head)
    printLinkedList(newHead)  
    
    t -= 1
