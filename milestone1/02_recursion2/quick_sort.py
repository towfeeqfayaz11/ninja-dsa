# quick sort -> also known as "partition exchange sort"
#            -> It uses a key element (pivot) for partitioning the elements.
#            -> One left partition contains all those elements that are smaller than the pivot and 
#               one right partition contains all those elements which are greater than the pivot element.
# quick sort vs merge sort
# quick sort is better than insertion, bubble and selection sort.
# quick sort is arguablly better than merge sort in some cases

# comparision: Merge sort is more efficient and works faster than quick sort in case of larger array size or datasets.whereas,
#              Quick sort is more efficient and works faster than merge sort in case of smaller array size or datasets

# time/space complexities: 
#     quick sort: O(n2),       inplace O(1)
#     merge sort: O(nlogn),    needs assitional space, O(n)  


# solution 1:
def quickSort(arr, start, end):
    if start >= end-1:              # array is empty or has only one element (array is sorted in that case)
        return
    
    pivot_index = partition(arr, start, end-1)
    quickSort(arr, start, pivot_index)
    quickSort(arr, pivot_index+1, end)
    

def partition(arr,si,ei):
    pivot = arr[si]
    
    c = 0
    for i in range(si,ei+1):
        if pivot > arr[i]:
            c+=1
    arr[si+c], arr[si] = arr[si],arr[si+c]
    pivot_index = si+c
    i,j = si,ei
    while i < j:
        if arr[i] < pivot:
            i+=1
        elif arr[j] >= pivot:
            j-=1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1
    return pivot_index

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n)
print(*arr)

# for num in arr:
# 	print(num, end=' ')
# print()
# ----------------------------------------------------------------------------------------

# solution 2:
def partition(a,si,ei):
    pivot=a[si]
    #find number of elements smaller than pivot
    c=0
    for i in range(si,ei+1):
        if a[i]<pivot:
            c=c+1
    a[si+c],a[si]=a[si],a[si+c]
    pivot_index=si+c
    
    i=si
    j=ei
    while i<j:
        if a[i]<pivot:
            i=i+1
        elif a[j]>=pivot:
            j=j-1
        else:
            a[i],a[j]=a[j],a[i]
            i=i+1
            j=j-1
    return pivot_index

def quick_sort(a,si,ei):
    if si>=ei:
        return
    
    pivot_index=partition(a,si,ei)
    quick_sort(a,si,pivot_index-1)
    quick_sort(a,pivot_index+1,ei)


a=[6,10,9,8,7,1,3,5,4,2]
print(partition(a,0,len(a)-1))


a=[6,10,9,8,7,1,3,5,4,2]
print(quick_sort(a,0,len(a)-1))
print(a)