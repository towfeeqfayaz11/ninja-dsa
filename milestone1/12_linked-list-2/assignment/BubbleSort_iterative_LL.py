# Bubble Sort (Iterative) LinkedList

# Given a singly linked list of integers, sort it using 'Bubble Sort.'
# Note :
# No need to print the list, it has already been taken care. Only return the new head to the list.
# Input format :
# The first and the only line of each test case or query contains the elements of the singly linked list separated by a single space.
# Remember/Consider :
# While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
# Output format :
# For each test case/query, print the elements of the sorted singly linked list.

# Output for every test case will be printed in a seperate line.
# Constraints :
# 0 <= M <= 10^3
# Where M is the size of the singly linked list.

# Time Limit: 1sec
# Sample Input 1 :
# 10 9 8 7 6 5 4 3 -1
# Sample Output 1 :
#  3 4 5 6 7 8 9 10 
#  Sample Input 2 :
# 10 -5 9 90 5 67 1 89 -1
# Sample Output 2 :
# -5 1 5 9 10 67 89 90 


##################################################################################


# solution:
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def length(head):
    curr=head
    count=0
    while curr is not None:
        curr=curr.next
        count+=1
    return count
        


# def swap_adjacent_nodes(prev,curr,nxt):
#     if prev == None:
#         prev = nxt.next
#         nxt.next = curr
#         curr.next = prev
        
#     else:
#         prev.next = nxt
#         curr.next = nxt.next
#         nxt.next = curr


def bubbleSort(head) :
	#Your code goes here
    n=length(head)
    for i in range(n-1):
        prev=None
        curr=head
        for j in range(n-i-1):
            if curr.data<=curr.next.data:
                prev=curr
                curr=curr.next
            else:
                if prev is None:
                    fwd=curr.next
                    head=head.next
                    curr.next=fwd.next
                    fwd.next=curr
                    prev=fwd
                else:
                    fwd=curr.next
                    prev.next=fwd
                    curr.next=fwd.next
                    fwd.next=curr
                    prev=fwd
    return head
                    
                    



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
head = takeInput()
head = bubbleSort(head)
printLinkedList(head)