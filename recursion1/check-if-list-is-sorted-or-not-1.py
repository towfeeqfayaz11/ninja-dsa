# check if list is sorted



# approach 1: first check       --> so we are doing check at start of array, if arr[0] <= arr[1]
def isSorted(arr: list) -> bool:
    l = len(arr)
    if l == 1 or l == 0:
        return True
    
    if arr[0] <= arr[1]:
        return isSorted(arr[1:])             # this code is inefficient in terms of memory use, as for each recursion call a new array is created
    else:
        return False



arr = list(map(int,input().split()))
print(isSorted(arr))

# ************************************************************************************************************************

# approach 2: last check        --> so we are doing check at end of array, if arr[n] >= arr[n-1]
def isSorted(arr: list) -> bool:
    l = len(arr)
    if l == 1 or l == 0:
        return True
    
    is_sorted = isSorted(arr[:-1])      # check if rest of array is sorted excepted for last element
                                         # this code is inefficient in terms of memory use, as for each recursion call a new array is created
    
    if is_sorted:
        return arr[-1] >= arr[-2]
    else:
        return False



arr = list(map(int,input().split()))
print(isSorted(arr))






# NOTE: in both the above approaches, we are creating a new array in each recursive call, which make it memory intensive, for better solution check file "check-if-list-is-sorted-or-not-2.py"

# NOTE: however if we have to compare above two approaches, approach 1 is better as in case of list is not sorted, since we are cheking before making new call, it will save some recursive calls





