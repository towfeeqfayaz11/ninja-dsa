# Find the Unique Element

# You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].
# Now, in the given array/list, 'M' numbers are present twice and one number is present only once.
# You need to find and return that number which is unique in the array/list.
#  Note:
# Unique element is always present in the array/list according to the given condition.
# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# First line of each test case or query contains an integer 'N' representing the size of the array/list.

# Second line contains 'N' single space separated integers representing the elements in the array/list.
# Output Format :
# For each test case, print the unique element present in the array.

# Output for every test case will be printed in a separate line.
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^6

# Time Limit: 1 sec
# Sample Input 1:
# 1
# 7
# 2 3 1 6 3 6 2
# Sample Output 1:
# 1
# Sample Input 2:
# 2
# 5
# 2 4 7 2 7
# 9
# 1 3 1 3 6 6 7 10 7
# Sample Output 2:
# 4
# 10

##############################################################################

# solution 1:
from sys import stdin
def findUnique(arr, n) :
    # using map
    mymap = {}
    for i,v in enumerate(arr):
        if v in mymap.keys():
            mymap[v]+=1
        else:
            mymap[v] = 1
    
    for k,v in mymap.items():
        if v == 1:
            return k


#taking input using fast I/O method
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
    print(findUnique(arr, n))

    t-= 1

##############################################################

# solution 2:
from sys import stdin
import functools
def findUnique(arr, n) :
	# using xor operator
    return functools.reduce(lambda a,b:a^b,arr)
    


#taking input using fast I/O method
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
    print(findUnique(arr, n))

    t-= 1


###################################################################
# solution 3:
from sys import stdin
def findUnique(arr, n) :
    # using xor operator
    res = 0
    for i in arr:
        res = res^i
    return res



#taking input using fast I/O method
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
    print(findUnique(arr, n))

    t-= 1