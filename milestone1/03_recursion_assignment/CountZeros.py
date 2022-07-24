# Count Zeros

# Given an integer N, count and return the number of zeros that are present in the given integer using recursion.
# Input Format :
# Integer N
# Output Format :
# Number of zeros in N
# Constraints :
# 0 <= N <= 10^9
# Sample Input 1 :
# 0
# Sample Output 1 :
# 1
# Sample Input 2 :
# 00010204
# Sample Output 2 :
# 2
# Explanation for Sample Output 2 :
# Even though "00010204" has 5 zeros, the output would still be 2 because when you convert it to an integer, it becomes 10204.
# Sample Input 3 :
# 708000
# Sample Output 3 :
# 4

# -----------------------------

# solution 1:
def count_zeros(n):
    if n>0 and n<10:
        return 0
    if n == 0:
        return 1
    if n % 10 == 0:
        return 1+count_zeros(n//10)
    else:
        return count_zeros(n//10)

# main
n = int(input())
print(count_zeros(n))

# -----------------------------

# solution 2: (considerring even for negative numbers)
def count_zeros(n):
    if n<0:
        n *= -1       # make n positive
    if n<10:
    	if n == 0:
    		return 1
    	return 0
    if n % 10 == 0:
        return 1+count_zeros(n//10)
    else:
        return count_zeros(n//10)

# main
n = int(input())
print(count_zeros(n))


