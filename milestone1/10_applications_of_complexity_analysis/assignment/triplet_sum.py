# Triplet sum

# You have been given a random integer array/list(ARR) and a number X. Find and return the triplet(s) in the array/list which sum to X.
# Note :
# Given array/list can contain duplicate elements.
# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# First line of each test case or query contains an integer 'N' representing the size of the first array/list.

# Second line contains 'N' single space separated integers representing the elements in the array/list.

# Third line contains an integer 'X'.
# Output format :
# For each test case, print the total number of triplets present in the array/list.

# Output for every test case will be printed in a separate line.
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^3
# 0 <= X <= 10^9

# Time Limit: 1 sec
# Sample Input 1:
# 1
# 7
# 1 2 3 4 5 6 7 
# 12
# Sample Output 1:
# 5
# Sample Input 2:
# 2
# 7
# 1 2 3 4 5 6 7 
# 19
# 9
# 2 -5 8 -6 0 5 10 11 -3
# 10
# Sample Output 2:
# 0
# 5


#  Explanation for Input 2:
# Since there doesn't exist any triplet with sum equal to 19 for the first query, we print 0.

# For the second query, we have 5 triplets in total that sum up to 10. They are, (2, 8, 0), (2, 11, -3), (-5, 5, 10), (8, 5, -3) 
# and (-6, 5, 11)



#########################################################################################################

# solution 1:
from sys import stdin

def tripletSum(arr, n, num) :
    #using unordered map (TC = n^2, sc=n)
    count = 0
    for i in range(n):
        mymap = {}
        curr = num - arr[i]
        for j in range(i+1,n):
            if curr - arr[j] in mymap:
                count+=mymap[curr-arr[j]]
            
            if arr[j] in mymap:
                mymap[arr[j]] +=1
            else:
                mymap[arr[j]] = 1
    return count



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
    num = int(stdin.readline().strip())
    print(tripletSum(arr, n, num))

    t -= 1




################################################################################

# solution 2:
from sys import stdin


def tripletSum(arr, n, num):
    arr.sort()
    numTriplets = 0
    for i in range(n):
        pairSumFor = num - arr[i]
        numPairs = pairSum(arr, (i + 1), (n - 1), pairSumFor)
        numTriplets += numPairs
    return numTriplets

def pairSum(arr, startIndex, endIndex, num):
    numPair = 0
    while startIndex < endIndex:
        if arr[startIndex] + arr[endIndex] < num:
            startIndex += 1
        elif arr[startIndex] + arr[endIndex] > num:
            endIndex -= 1
        else:
            elementAtStart = arr[startIndex]
            elementAtEnd = arr[endIndex]
            if elementAtStart == elementAtEnd:
                totalElementsFromStartToEnd = (endIndex - startIndex) + 1
                numPair += (totalElementsFromStartToEnd * (totalElementsFromStartToEnd - 1) // 2)
                return numPair
            tempStartIndex = startIndex + 1
            tempEndIndex = endIndex - 1
            while (tempStartIndex <= tempEndIndex) and (arr[tempStartIndex] == elementAtStart):
                tempStartIndex += 1
            while (tempEndIndex >= tempStartIndex) and (arr[tempEndIndex] == elementAtEnd):
                tempEndIndex -= 1
            totalElementsFromStart = (tempStartIndex - startIndex)
            totalElementsFromEnd = (endIndex - tempEndIndex)
            numPair += (totalElementsFromStart * totalElementsFromEnd)
            startIndex = tempStartIndex
            endIndex = tempEndIndex
    return numPair

        



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
    num = int(stdin.readline().strip())
    print(tripletSum(arr, n, num))

    t -= 1



