# time complexity : O(nlogn)
# space complexity: O(n)

# solution 1:

def mergeSort(arr, start, end):
    if end == 0 or end == 1:
        return
    mid = end//2
    a1 = arr[start:mid]
    a2 = arr[mid:end]
    mergeSort(a1, start, mid)
    mergeSort(a2, 0, len(a2))
    merge(a1,a2,arr)

def merge(a1,a2,arr):
    i,j,k = 0,0,0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            arr[k] = a1[i]
            i+=1
            k+=1
        else:
            arr[k] = a2[j]
            j+=1
            k+=1
    while i < len(a1):
        arr[k] = a1[i]
        i+=1
        k+=1
    while j < len(a2):
        arr[k] = a2[j]
        j+=1
        k+=1
    
        
# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr, 0, n)
print(*arr)


# ---------------------------------------------------------------------------------

# solution 2:
def mergeSort(arr, start, end):
    size = end-start
    if size <= 1:
        return
    mid = (start+end)//2
    mergeSort(arr, start, mid)
    mergeSort(arr, mid, end)
    

    # merge two sorted arrays
    result = [0]*size
    i,j,k = start,mid,0

    while i < mid and j < end:
        if arr[i] < arr[j]:
            result[k] = arr[i]
            i+=1
            k+=1
        else:
            result[k] = arr[j]
            j+=1
            k+=1
    while i < mid:
        result[k] = arr[i]
        i+=1
        k+=1
    while j < end:
        result[k] = arr[j]
        j+=1
        k+=1
    
    # updating arr
    for i in range(0,size):
    	arr[start+i] = result[i]

    
        
# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr, 0, n)
for num in arr:
	print(num,end=' ')
print()