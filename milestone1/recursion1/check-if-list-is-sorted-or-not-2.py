def isSortedBetter(arr: list, si: int) -> bool:        # "si" is the starting index
	arr_l = len(arr)
	if si == arr_l - 1 or si == arr_l:           # if index is 0 or len of array is zero
		return True

	if arr[si] <= arr[si+1]:
		return isSortedBetter(arr,si+1)          # this approach is better than code in file "check-if-list-is-sorted-or-not-1.py" as we are not creating new array in each recusrion call, rather passing same array as reference
	else:
		return False


if __name__ == "__main__":
	arr = list(map(int,input().split()))
	res = isSortedBetter(arr,0)
	print(res)
