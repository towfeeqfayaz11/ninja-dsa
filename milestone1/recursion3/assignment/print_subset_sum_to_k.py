# Print Subset Sum to K

# Given an array A and an integer K, print all subsets of A which sum to K.
# Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.
# Note : The order of subsets are not important. Just print them in different lines.
# Input format :
# Line 1 : Size of input array
# Line 2 : Array elements separated by space
# Line 3 : K 
# Sample Input:
# 9 
# 5 12 3 17 1 18 15 3 17 
# 6
# Sample Output:
# 3 3
# 5 1

# ---------------------------------------------

# solution
def printSubset(arr,k,res):
    if len(arr) == 0:
        if k == 0:
            for i in res:
                for j in i:
                    print(j,end=' ')
                print()
            return
        else:
            return
    
    temp = res.copy()
    res2 = []
    for i in temp:
        res2.append(i+[arr[0]])
    printSubset(arr[1:],k-arr[0],res2)
    printSubset(arr[1:],k,res)
    

# main
n = int(input())
arr = list(map(int,input().split()))
k = int(input())
printSubset(arr,k,[[]])


