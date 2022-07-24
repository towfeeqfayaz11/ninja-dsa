# Eliminate duplicates from LL

# You have been given a singly linked list of integers where the elements are sorted in ascending order. Write a function that 
# removes the consecutive duplicate values such that the given list only contains unique elements and returns the head to the updated list.
#  Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# The first and the only line of each test case or query contains the elements(in ascending order) of the singly linked list separated by a single space.
#  Remember/Consider :
# While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element.
#  Output format :
# For each test case/query, print the resulting singly linked list of integers in a row, separated by a single space.

# Output for every test case will be printed in a seperate line.
# Constraints :
# 1 <= t <= 10^2
# 0 <= M <= 10^5
# Time Limit: 1sec

# Where 'M' is the size of the singly linked list.
# Sample Input 1 :
# 1
# 1 2 3 3 3 3 4 4 4 5 5 7 -1
# Sample Output 1 :
# 1 2 3 4 5 7 
# Sample Input 2 :
# 2
# 10 20 30 40 50 -1
# 10 10 10 10 -1
# Sample Output 2 :
# 10 20 30 40 50
# 10



#############################################################################


# solution 1:

from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)


#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



# recursive
def removeDuplicates(head):
    # increase recursion limit for this code, otherwise it will give runtime error
    if head == None or head.next == None:     # if LL has zero or single element
        return head
    
    smallHead = removeDuplicates(head.next)
    if head.data == smallHead.data:
        head.next = None
        return smallHead
    else:
        head.next = smallHead
        return head
 

# iterative
 def removeDuplicates(head): 
    if head == None or head.next == None:
        return head
    
    t1 = head
    t2 = head.next
    
    while t2.next != None:
        if t1.data == t2.data:
            t2 = t2.next
        else:
            t1.next = t2
            t1 = t2
            t2 = t2.next
            
        if t1.data == t2.data:
            t1.next = None
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


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    head = takeInput()

    head = removeDuplicates(head)
    printLinkedList(head)

    t -= 1