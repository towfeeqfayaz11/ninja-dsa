# Reverse the First K Elements in the Queue

# For a given queue containing all integer data, reverse the first K elements.
# You have been required to make the desired change in the input queue itself.
# Example:
# alt txt

# For the above input queue, if K = 4 then after reversing the first 4 elements, the queue will be updated as:
# alt txt

# Input Format :
# The first line of inzxput would contain two integers N and K, separated by a single space. They denote the total 
# number of elements in the queue and the count with which the elements need to be reversed respectively.

# The second line of input contains N integers separated by a single space, representing the order in which the elements 
# are enqueued into the queue.

# Output Format:
# The only line of output prints the updated order in which the queue elements are dequeued, all of them separated by a single space. 

# Note:
# You are not required to print the expected output explicitly, it has already been taken care of. Just make the changes 
# in the input queue itself.

# Contraints :
# 1 <= N <= 10^6
# 1 <= K <= N
# -2^31 <= data <= 2^31 - 1

#  Time Limit: 1sec
# Sample Input 1:
# 5 3
# 1 2 3 4 5
# Sample Output 1:
# 3 2 1 4 5
# Sample Input 2:
# 7 7
# 3 4 2 5 6 7 8
# Sample Output 2:
# 8 7 6 5 2 4 3




###############################################################################


# solution


from sys import stdin
import queue

def reverseKElements(inputQueue, k) :
    #taking help of stack for k reverse
    stack = []
    
    # step 1: push k elements from queue to stack
    for _ in range(k):
        stack.append(inputQueue.get())
    
    # step 2: now enqueue k elements from stack back to queue (and they k elements will be in reversed order)
    while stack:
        inputQueue.put(stack.pop())
    
    # step 3: after step two, we have k elements reversed in queue, but they are at end of the queue
    # we need to Dequeue (size-k) elements from the front and enqueue them one by one to the same queue.
    
    size = inputQueue.qsize()
    
    for _ in range(size-k):
        ele = inputQueue.get()
        inputQueue.put(ele)
    
    # finally we have k reversed elements in queue
    return inputQueue





'''-------------- Utility Functions --------------'''


#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Takes a list as a stack and returns the element at the top
def top(stack) :
    #assuming the stack is never empty
    return stack[len(stack) - 1]



def takeInput():
    n_k = list(map(int, stdin.readline().strip().split(" ")))
    n = n_k[0]
    k = n_k[1]

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return k, qu


#main
k, qu = takeInput()

qu = reverseKElements(qu, k)

while not qu.empty() :
    print(qu.get(), end = " ")
