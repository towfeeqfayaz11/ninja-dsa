# Check Number in Array

# Given an array of length N and an integer x, you need to find if x is present in the array or not. Return true or false.
# Do this recursively.

# Input Format :
# Line 1 : An Integer N i.e. size of array
# Line 2 : N integers which are elements of the array, separated by spaces
# Line 3 : Integer x

# Output Format :
# 'true' or 'false'

# Constraints :
# 1 <= N <= 10^3

# Sample Input 1 :
# 3
# 9 8 10
# 8
# Sample Output 1 :
# true

# Sample Input 2 :
# 3
# 9 8 10
# 2
# Sample Output 2 :
# false

# *************************************************************************************

# solution 1:
def x_exists(arr,si,arr_l,x):
    if si == arr_l:
        return "false"
    
    if x == arr[si]:
        return "true"
    else:
        return x_exists(arr,si+1,arr_l,x)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    # arr=list(int(i) for i in input().strip().split(' '))
    x = int(input())
    res = x_exists(arr,0,n,x)
    print(res)