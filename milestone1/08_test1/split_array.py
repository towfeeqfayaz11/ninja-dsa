# Split Array

# Given an integer array A of size N, check if the input array can be splitted in two parts such that -
# - Sum of both parts is equal
# - All elements in the input, which are divisible by 5 should be in same group.
# - All elements in the input, which are divisible by 3 (but not divisible by 5) should be in other group.
# - Elements which are neither divisible by 5 nor by 3, can be put in any group.
# Groups can be made with any set of elements, i.e. elements need not to be continuous. And you need to consider each and every element of input array in some group.
# Return true, if array can be split according to the above rules, else return false.
# Note : You will get marks only if all the test cases are passed.
# Input Format :
# Line 1 : Integer N (size of array)
# Line 2 : Array A elements (separated by space)
# Output Format :
# true or false
# Constraints :
# 1 <= N <= 50
# Sample Input 1 :
# 2
# 1 2
# Sample Output 1 :
# false
# Sample Input 2 :
# 3
# 1 4 3
# Sample Output 2 :
# true


# solution1:
# recursive function to return truw if array can be split into two sub arrays based on given condition
def split(arr,i,n,lsum,rsum):
    # if end of array is reached return result
    if i == n:
        return lsum == rsum
    
    # if element is divisible by 5, add to lsum
    if arr[i] % 5 == 0:
        lsum+=arr[i]
    
    # if element is divisible by 3 (but not by 5) add to rsum
    elif arr[i] % 3 == 0:
        rsum+=arr[i]
        
    # for element neither divisible by 5 or 3, check by adding to both lsum and rsum one by one to confirm if it satisfies the consition
    else:
        return split(arr, i+1, n, lsum+arr[i], rsum) or split(arr, i+1, n, lsum, rsum+arr[i])
    
    
    # for cases when element is multiple of 5 or 3
    return split(arr,i+1,n,lsum,rsum)
    
        
    
    
    
    
n = input()
arr = [int(ele) for ele in input().split()]
ans = split(arr,0,len(arr),0,0)
if ans is True:
    print('true')
else:
    print('false')





# soluton2:
def split(arr,i,sum):
    
    if i == len(arr):
    	if sum == 0:
    		return True
    	else:
    		return False

    if ((arr[i]%5) == 0):
    	return split(arr,i+1,sum+arr[i])
    elif ((arr[i]%3) == 0):
    	return split(arr,i+1,sum-arr[i])
    else:
    	ans1 = split(arr,i+1,sum+arr[i])
    	ans2 = split(arr,i+1,sum-arr[i])
    	return ans1 or ans2
    
    
n = input()
arr = [int(ele) for ele in input().split()]
ans = split(arr,0,0)
if ans is True:
    print('true')
else:
    print('false')
