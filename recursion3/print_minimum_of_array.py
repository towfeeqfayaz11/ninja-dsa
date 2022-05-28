#

def printMin(arr, minSoFar):
  if len(arr) == 0:
    print(minSoFar)
    return
  minSoFar = min(minSoFar,arr[0])
  printMin(arr[1:], minSoFar)



arr = list(map(int,input().split()))
printMin(arr,float("inf"))             # passing float value of infinity as default instead of intmax


# --------------------------------------------------
# return minimum of an array
import sys
def returnMin(arr):
	if len(arr) == 0:
		return float("inf")

	aux_minimum = returnMin(arr[1:])
	overallMin = min(aux_output,arr[0])
	return overallMin


arr = list(map(int,input().split()))
print(returnMin(arr))


# -----------------------
# If you are looking for a number that is bigger than all others:

# Method 1:
# float('inf')

# Method 2:
# import sys
# max = sys.maxsize


# If you are looking for a number that is smaller than all others:

# Method 1:
# float('-inf')

# Method 2:
# import sys
# min = -sys.maxsize - 1
# -----------------------