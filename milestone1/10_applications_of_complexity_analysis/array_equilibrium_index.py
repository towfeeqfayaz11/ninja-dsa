# Array Equilibrium Index

# For a given array/list(ARR) of size 'N,' find and return the 'Equilibrium Index' of the array/list.
# Equilibrium Index of an array/list is an index 'i' such that the sum of elements at indices [0 to (i - 1)] is equal to the 
# sum of elements at indices [(i + 1) to (N-1)]. One thing to note here is, the item at the index 'i' is not included in either part.

# If more than one equilibrium indices are present, then the index appearing first in left to right fashion should be returned. 
# Negative one(-1) if no such index is present.

# Example:
# Let's consider an array/list Arr = [2, 3, 10, -10, 4, 2, 9]  of size, N = 7.

# There exist three equilibrium indices, one at 2, another at 3, and another at 5.

# At index 2, the sum of all the elements to the left, [2 + 3] is 5, and the elements to its right, [-10 + 4 + 2 + 9] is also 5. 
# Hence index 2 is an equilibrium index according to the condition we want to achieve. Mind it that we haven't included the item 
# at index 2, which is 10, to either of the parts.

# Similarly, we can see at index 3 and 5, the elements to its left sum up to 15 and 9 respectively and to the right, sum up 
# to 15 and 9 respectively either. 

# Hence the answer would be 3.
# Input Format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# The first line of each test case or query contains an integer 'N' representing the size of the first array/list.

# The second line contains 'N' single space separated integers representing the elements of the array/list
# Output Format :
# For each test case, print the 'Equilibrium Index'.

# Output for every test case will be printed in a separate line.
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^6

# Time Limit: 1 sec 
# Sample Input 1 :
# 1
# 5
# 1 4 9 3 2
# Sample Output 1 :
# 2
# Sample Input 2 :
# 2
# 3
# 1 4 6
# 3
# 1 -1 4
# Sample Output 2 :
# -1
# 2

##############################################################################################################################



# solution1:
from sys import stdin
def arrayEquilibriumIndex(arr, n) :
    if n == 0:
        return -1
    if n == 1:
        return 1
    
    l_sum, r_sum = 0,sum(arr[1:])
    i = 0
    while i<n-1:
        if l_sum == r_sum:
            return i
        l_sum+=arr[i]
        i+=1
        r_sum-=arr[i]
    return -1


#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(arrayEquilibriumIndex(arr, n))

    t-= 1




#####################################################################################################

# solution2:
from sys import stdin

def arrayEquilibriumIndex(arr, n) :
    if n == 0:
        return -1
    if n == 1:
        return 1
    
    l_sum, r_sum = 0,sum(arr[1:])
    i = 0
    for i in range(1,n):
        if l_sum == r_sum:
            return i-1
        l_sum+=arr[i-1]
        r_sum-=arr[i]
    
    if sum(arr[:n-2]) == 0:
        return n-1
        
    return -1


#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(arrayEquilibriumIndex(arr, n))

    t-= 1