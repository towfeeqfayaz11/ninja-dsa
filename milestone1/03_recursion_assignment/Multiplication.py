# Multiplication (Recursive)

# Given two integers M & N, calculate and return their multiplication using recursion. You can only use subtraction and addition for your calculation. No other operators are allowed.
# Input format :
# Line 1 : Integer M
# Line 2 : Integer N
# Output format :
# M x N
# Constraints :
# 0 <= M <= 1000
# 0 <= N <= 1000
# Sample Input 1 :
# 3 
# 5
# Sample Output 1 :
# 15
# Sample Input 2 :
# 4 
# 0
# Sample Output 2 :
# 0

# ------------------------------------------------

# solution

from sys import setrecursionlimit
setrecursionlimit(10**6)

def multiplication(m,n):
    if n == 0:
        return 0             # in multiplicaton, if either of the number is 0, the ans is 0
    
    return m + multiplication(m,n-1)

m = int(input())
n = int(input())
print(multiplication(m,n))