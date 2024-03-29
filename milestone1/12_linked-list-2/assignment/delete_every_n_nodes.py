# Delete every N nodes

# You have been given a singly linked list of integers along with two integers, 'M,' and 'N.' Traverse the linked list 
# such that you retain the 'M' nodes, then delete the next 'N' nodes. Continue the same until the end of the linked list.

# To put it in other words, in the given linked list, you need to delete N nodes after every M nodes.
# Note :
# No need to print the list, it has already been taken care. Only return the new head to the list.
# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# The first line of each test case or query contains the elements of the singly linked list separated by a single space.

# The second line of input contains two integer values 'M,' and 'N,' respectively. A single space will separate them.
#  Remember/Consider :
# While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
# Output format :
# For each test case/query, print the elements of the updated singly linked list.

# Output for every test case will be printed in a seperate line.
# Constraints :
# 1 <= t <= 10^2
# 0 <= P <= 10^5
# Where P is the size of the singly linked list.
# 0 <= M <= 10^5
# 0 <= N <= 10^5 

# Time Limit: 1sec
# Sample Input 1 :
# 1
# 1 2 3 4 5 6 7 8 -1
# 2 2
# Sample Output 1 :
# 1 2 5 6
# Sample Input 2 :
# 2
# 10 20 30 40 50 60 -1
# 0 1
# 1 2 3 4 5 6 7 8 -1
# 2 3
# Sample Output 2 :
# 1 2 6 7
# Explanation of Sample Input 2 :
# For the first query, we delete one node after every zero elements hence removing all the items of the list. Therefore, nothing got printed.

# For the second query, we delete three nodes after every two nodes, resulting in the final list, 1 -> 2 -> 6 -> 7.


##################################################################################


# solution 1:
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def skipMdeleteN(head, M, N) :
    if head is None:
        return None
    if M == 0:
        return None
    if N == 0:
        return head
    
    head
    t1, t2 = head,head
    while t1 and t2:
        c1,c2 = 1,0
        while c1 < M and t1:
            t1 = t1.next
            c1+=1
        if t1 is None:
            continue
        t2 = t1.next
        while c2 < N and t2:
            t2 = t2.next
            c2+=1
        
        t1.next = t2
        
        t1 = t2
    
    return head
        

# solution2
def skipMdeleteN(head, M, N) :
    if head is None or M == 0:
        return None
    if N == 0:
        return head
    
    currNode = head
    temp = None
    while currNode is not None:
        take=0
        skip=0
        while currNode is not None and take > M:
            if temp is None:
                temp = currNode
            else:
                temp.next = currNode
                temp = currNode

            currNode = currNode.next
            take+=1

        while currNode is not None and skip < N:
            currNode = currNode.next
            skip+=1
    
    if temp is not None:
        temp.next = None
        
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
    m_n = stdin.readline().strip().split(" ")

    m = int(m_n[0])
    n = int(m_n[1])

    newHead = skipMdeleteN(head, m, n)
    printLinkedList(newHead)

    t -= 1










