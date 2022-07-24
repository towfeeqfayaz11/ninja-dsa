# Duplicate in array

# You have been given an integer array/list(ARR) of size N which contains numbers from 0 to (N - 2). Each number is present at least once. That is, if N = 5, the array/list constitutes values ranging from 0 to 3, and among these, there is a single integer value that is present twice. You need to find and return that duplicate number present in the array.
# Note :
# Duplicate number is always present in the given array/list.
# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# First line of each test case or query contains an integer 'N' representing the size of the array/list.

# Second line contains 'N' single space separated integers representing the elements in the array/list.
# Output Format :
# For each test case, print the duplicate element in the array/list.

# Output for every test case will be printed in a separate line.
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^6

# Time Limit: 1 sec
# Sample Input 1:
# 1
# 9
# 0 7 2 5 4 7 1 3 6
# Sample Output 1:
# 7
# Sample Input 2:
# 2
# 5
# 0 2 1 3 1
# 7
# 0 3 1 5 4 3 2
# Sample Output 2:
# 1
# 3

#################################################################

# solution 1:
from sys import stdin


def findDuplicate(arr, n) :
    arr.sort()
    i,j = 0,1
    while j<n:
        if arr[i] == arr[j]:
            return arr[i]
        i+=1
        j+=1
   
#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip()) 

while t > 0 :

    arr, n = takeInput()
    print(findDuplicate(arr, n))

    t -= 1



####################################################################
# solution 2:

from sys import stdin


def findDuplicate(arr, n) :
    # using the info that array contains numbers from 0 to (N - 2)
    sum_arr = sum(arr)
    # sum pf first n-2 natural numbers
    sum_of_n_2 = (n-2)*(n-1)//2
    
    return sum_arr - sum_of_n_2
    

#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip()) 

while t > 0 :

    arr, n = takeInput()
    print(findDuplicate(arr, n))

    t -= 1