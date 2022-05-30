# Return subsets sum to K

# Given an array A of size n and an integer K, return all subsets of A which sum to K.
# Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.
# Note : The order of subsets are not important.
# Input format :
# Line 1 : Integer n, Size of input array
# Line 2 : Array elements separated by space
# Line 3 : K 
# Constraints :
# 1 <= n <= 20
# Sample Input :
# 9 
# 5 12 3 17 1 18 15 3 17 
# 6
# Sample Output :
# 3 3
# 5 1

# ---------------------------------------------------------------

import sys
sys.setrecursionlimit(10 ** 8)


def subsetsSumK(arr, k) :
    #Your code goes here
    if len(arr) == 0:
        if k == 0:
            return [[]]
        else:
            return []
    output1 = subsetsSumK(arr[1:], k-arr[0])
    output2 = subsetsSumK(arr[1:], k)
    output = []
    for i in output1:
        output.append([arr[0]]+i)
    for j in output2:
        output.append(j)
    return output


#taking input
def takeInput() :
    n = int(input().strip())

    if n == 0 :
        return list(), 0

    arr = [int(element) for element in list(input().strip().split(" "))]
    return arr, n


#printing the list of lists
def printListOfList(liOfLi) :
    for li in liOfLi :
        for elem in li :
            print(elem, end = " ")
        print()

#main
arr, n = takeInput()

if n != 0 :
    k = int(input().strip())
    liOfLi = subsetsSumK(arr, k)

    printListOfList(liOfLi)