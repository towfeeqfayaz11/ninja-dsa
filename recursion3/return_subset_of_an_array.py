# Return subset of an array

# Given an integer array (of length n), find and return all the subsets of input array.
# Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.
# Note : The order of subsets are not important.
# Input format :

# Line 1 : Size of array

# Line 2 : Array elements (separated by space)

# Sample Input:
# 3
# 15 20 12
# Sample Output:
# [] (this just represents an empty array, don't worry about the square brackets)
# 12 
# 20 
# 20 12 
# 15 
# 15 12 
# 15 20 
# 15 20 12 

# ------------------------------------------------------------------

solution:
def ArraySubset(arr):
    if len(arr) == 0:
        return [[]]
    smallOutput = ArraySubset(arr[1:])
    output = []
    for i in smallOutput:
        output.append(i)
    for j in smallOutput:
        output.append([arr[0]]+j)
    return output
    


# main
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    ans = ArraySubset(arr)
    for i in ans:
        for j in i:
            print(j,end=" ")
        print()
