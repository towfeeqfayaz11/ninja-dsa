# given an array arr and a number x, return the index of the last occurance of x in array, if not present return -1


# solution 1                   # creating array copies   (searching from last to first)
def last_index(arr,x):
    arr_l = len(arr)
    if arr_l == 0:
        return -1
    
    if arr[arr_l-1] == x:
        return arr_l-1
    
    smallerListOutput = last_index(arr[:arr_l-1],x)               # creating array copy in each iteration call 
    
    return smallerListOutput


if __name__ == "__main__":
    n = int(input())
    arr = list(int(i) for i in input().split())
    x = int(input())
    res = last_index(arr,x)
    print(res)

# *********************************************************************************

# solution 2                 # without creating array copies (searching from last to first)
def last_index(arr,x,arr_l):
    if arr_l == 0:
        return -1
    
    if arr[arr_l-1] == x:
        return arr_l-1
    
    smallerListOutput = last_index(arr,x,arr_l-1)          # not creating array copies
    
    return smallerListOutput


if __name__ == "__main__":
    n = int(input())
    arr = list(int(i) for i in input().split())
    x = int(input())
    res = last_index(arr,x,n)
    print(res)

# ***********************************************************************************

# solution 3                    # without creating array copies (searching from first to last)
def last_index(arr,x,si):
    if si == len(arr):
        return -1
    
    smallerListOutput = last_index(arr,x,si+1)

    if smallerListOutput == -1 and arr[si] == x:
        return si
    else:
        return smallerListOutput

if __name__ == "__main__":
    n = int(input())
    arr = list(int(i) for i in input().split())
    x = int(input())
    prev = -1
    res = last_index(arr,x,0)
    print(res)
# ***********************************************************************************

# solution 4                    # creating array copies (searching from first to last)
def last_index(arr,x):
    if len(arr) == 0:
        return -1

    smallerListOutput = last_index(arr[1:],x)

    if smallerListOutput != -1:
        return smallerListOutput+1
    else:
    	if arr[0] == x:
    		return 0
    	else:
    		return -1

# def lastIndex(arr,x,si):                # covers edge cases much better
#     l=len(arr)
#     if si==l:
#         return -1
#     smallerListOutput=lastIndex(arr,x,si+1)
#     if smallerListOutput!=-1:
#         return smallerListOutput
#     else:
#         if arr[si]==x:
#             return si
#         else:
#             return -1


if __name__ == "__main__":
    n = int(input())
    arr = list(int(i) for i in input().split())
    x = int(input())
    prev = -1
    res = last_index(arr,x)
    print(res)