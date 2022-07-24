# Array Intersection

# You have been given two integer arrays/list(ARR1 and ARR2) of size N and M, respectively. You need to print their intersection; 
# An intersection for this problem can be defined when both the arrays/lists contain a particular value or to put it in other words, when there is a common value that exists in both the arrays/lists.
# Note :
# Input arrays/lists can contain duplicate elements.

# The intersection elements printed would be in the order they appear in the first sorted array/list(ARR1).


# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# The first line of each test case or query contains an integer 'N' representing the size of the first array/list.

# The second line contains 'N' single space separated integers representing the elements of the first the array/list.

# The third line contains an integer 'M' representing the size of the second array/list.

# The fourth line contains 'M' single space separated integers representing the elements of the second array/list.
# Output format :
# For each test case, print the intersection elements in a row, separated by a single space.

# Output for every test case will be printed in a separate line.
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^6
# 0 <= M <= 10^6

# Time Limit: 1 sec 
# Sample Input 1 :
# 2
# 6
# 2 6 8 5 4 3
# 4
# 2 3 4 7 
# 2
# 10 10
# 1
# 10
# Sample Output 1 :
# 2 3 4
# 10
# Sample Input 2 :
# 1
# 4
# 2 6 1 2
# 5
# 1 2 3 4 2
# Sample Output 2 :
# 1 2 2
# Explanation for Sample Output 2 :
# Since, both input arrays have two '2's, the intersection of the arrays also have two '2's. The first '2' of first 
# array matches with the first '2' of the second array. Similarly, the second '2' of the first array matches with the 
# second '2' if the second array.


# solution1:
from sys import stdin

def quickSort(arr,start,end):
    if start >= end :
        return 
    
    pivot_index = partition(arr,start,end-1)
    quickSort(arr,start,pivot_index)
    quickSort(arr,pivot_index+1,end)
    
    
def partition(arr,si,ei):
    pivot = arr[si]
    
    c = 0
    for i in range(si,ei+1):
        if pivot > arr[i]:
            c+=1
    arr[si+c],arr[si] = arr[si],arr[si+c]
    pivot_index = si+c
    
    i,j = si,ei
    while i < j:
        if arr[i] < pivot:
            i+=1
        elif arr[j] >= pivot:
            j-=1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1
    return pivot_index
    
def intersection(arr1, arr2, n, m) :
    quickSort(arr1,0,n)
    quickSort(arr2,0,m)
    
    i,j = 0,0
    while i<n and j <m:
        if arr1[i] == arr2[j]:
            print(arr1[i], end=' ')
            i+=1
            j+=1
        elif arr1[i] > arr2[j]:
            j+=1
        else:
            i+=1




# Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    
    if n == 0 :
    	return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().strip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()
    intersection(arr1, arr2, n, m)
    print()

    t -= 1


