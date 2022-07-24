# given an array arr and a number x, return the index of the first occurance of x in array, if not present return -1



# solution 1: without copying the array multiple times
def first_index(arr,si,arr_l,x):
    if si == arr_l:
        return -1
    
    if arr[si] == x:
        return si
    else:
        return first_index(arr,si+1,arr_l,x)

if __name__ == "__main__":
    arr = list(int(i) for i in input().split())
    x = int(input())
    arr_l = len(arr)
    print(first_index(arr,0,arr_l,x))




# solution 2: copying the array to each iteration call
def first_index(arr,x):
    if len(arr) == 0:
        return -1
    
    if arr[0] == x:
        return 0
    
    sub_ans = first_index(arr[1:],x)
    
    if sub_ans == -1:
        return sub_ans
    else:
        return sub_ans+1

if __name__ == "__main__":
    arr = list(int(i) for i in input().split())
    x = int(input())
    arr_l = len(arr)
    print(first_index(arr,x))