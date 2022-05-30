# Sum Of Array

# Given an array of length N, you need to find and return the sum of all elements of the array.
# Do this recursively.

# Input Format :
# Line 1 : An Integer N i.e. size of array
# Line 2 : N integers which are elements of the array, separated by spaces

# Output Format :
# Sum
# Constraints :
# 1 <= N <= 10^3

# Sample Input 1 :
# 3
# 9 8 9
# Sample Output 1 :
# 26

# Sample Input 2 :
# 3
# 4 2 1
# Sample Output 2 :
# 7    

# ***************************************************************************************************

# solution 1:           # better approach

def array_sum(arr,si,arr_len):
    if si == arr_len-1:
        return arr[si]
    elif si == arr_len:
        return 0
    
    sub_arr_sum = array_sum(arr,si+1,arr_len)
    
    return arr[si] + sub_arr_sum



if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    
    res = array_sum(arr,0,n)     # passing arr, starting index, length
    print(res)

# ****************************************************************************************************

# solution 2:       # not good approach as we are creating copy of array in each recursion call

def sumArray(arr):
    # Please add your code here
    if len(arr) == 1:
        return arr[0]
    small_result = sumArray(arr[1:])
    result = arr[0] + small_result
    return result

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))
