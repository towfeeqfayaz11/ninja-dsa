# Swap two Nodes of LL

# You have been given a singly linked list of integers along with two integers, 'i,' and 'j.' Swap the nodes that are present 
# at the 'i-th' and 'j-th' positions.

# Note :
# Remember, the nodes themselves must be swapped and not the datas.

# No need to print the list, it has already been taken care. Only return the new head to the list.
# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# The first line of each test case or query contains the elements of the singly linked list separated by a single space.

# The second line of input contains two integer values 'i,' and 'j,' respectively. A single space will separate them.
#  Remember/consider :
# While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
# Output format :
# For each test case/query, print the elements of the updated singly linked list.

# Output for every test case will be printed in a seperate line.
# Constraints :
# 1 <= t <= 10^2
# 0 <= M <= 10^5
# Where M is the size of the singly linked list.
# 0 <= i < M
# 0 <= j < M

# Time Limit: 1sec
# Sample Input 1 :
# 1
# 3 4 5 2 6 1 9 -1
# 3 4
# Sample Output 1 :
# 3 4 5 6 2 1 9 
#  Sample Input 2 :
# 2
# 10 20 30 40 -1
# 1 2
# 70 80 90 25 65 85 90 -1
# 0 6
#  Sample Output 2 :
# 10 30 20 40 
# 90 80 90 25 65 85 70 


##############################################################################################

# solution 1:
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
def swapNodes(head, i, j) :
	#Your code goes here
    if i==j:
        return head
    curr=head
    prev=previ=curri=prevj=currj=None
    c=0
    while curr!=None:
        if c==i:
            previ=prev
            curri=curr
        elif c==j:
            prevj=prev
            currj=curr
        prev=curr
        curr=curr.next
        c+=1
    if curri==None or currj==None:
        return 
    if previ==None:
        head=currj
    else:
        previ.next=currj
    if prevj==None:
        head=curri
    else:
        prevj.next=curri
    curr=curri.next
    curri.next=currj.next
    currj.next=curr
    return head            


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
    i_j = stdin.readline().strip().split(" ")

    i = int(i_j[0])
    j = int(i_j[1])

    newHead = swapNodes(head, i, j)
    printLinkedList(newHead)

    t -= 1




#####################################################################################


 # solution 2:
 from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None      

def swapNodes(head, i, j) :
	#Your code goes here
    if head is None or head.next is None or i == j:
        return head
    
    p1,c1,x = None,head,0
    # point to prev and curr of i
    while c1 != None and x != i:
        p1 = c1
        c1 = c1.next
        x+=1
    
    p2,c2,y = None,head,0
    # pointing to prev and curr of j
    while c2 != None and y != j:
        p2 = c2
        c2 = c2.next
        y+=1
    
    # one of the element is not in the list and hence swap is not possible
    if c1 is None or c2 is None:
        return head
    
    # p1.next = c2
    # p2.next = c1
    # temp = c1.next
    # c1.next = c2.next
    # c2.next = temp
    
    if p1 is None:
        head = c2
    else:
        p1.next = c2
    
    if p2 is None:
        head = c1
    else:
        p2.next = c1
    
    temp = c1.next
    c1.next = c2.next
    c2.next = temp
    
    return head        


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
    i_j = stdin.readline().strip().split(" ")

    i = int(i_j[0])
    j = int(i_j[1])

    newHead = swapNodes(head, i, j)
    printLinkedList(newHead)

    t -= 1