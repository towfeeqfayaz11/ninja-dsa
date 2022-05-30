# given a sorted array and a key, return the index of the key from array if present, else return -1
# implement using both recursive and iteratively



# recursive solution:
def binaySearch(arr,x,si,ei) -> int:
	if si > ei:
		return -1
	mid = (si+ei) // 2
	if arr[mid] == x:
		return mid
	elif arr[mid] > x:
		return binaySearch(arr,x,si,mid-1):
	else:
		return binaySearch(arr,mid+1,ei):

if __name__ == "__main__":
	# the input array for binary search should be always sorted
	arr = list(map(int,input().split()))
	x = int(input())
	index = binaySearch(arr,x,0,len(arr)-1)
	print(index)


# ------------------------------------------------------------------------

# iterative solution:
def binarySearch(arr,x,si,ei) -> int:
	while si <= ei:
		mid = (si+ei)//2
		if arr[mid] == x:
			return mid
		elif arr[mid] < x:
			si = mid+1
		else:
			ei = mid-1
	return -1

if __name__ == "__main__":
	# the input array for binary search should be always sorted
	arr = list(map(int,input().split()))
	x = int(input())
	index = binaySearch(arr,x,0,len(arr)-1)
	print(index)