# Staircase

# A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up to the stairs. You need to return number of possible ways W.
# Input format :
# Integer N
# Output Format :
# Integer W
# Constraints :
# 1 <= N <= 30
# Sample Input 1 :
# 4
# Sample Output 1 :
# 7
# Sample Input 2 :
# 5
# Sample Output 2 :
# 13

# ----------------------------------------

# solution

def staircase(n):
    if n <=1:
        if n <0:
            return 0
        return 1
    res1 = staircase(n-1)
    res2 = staircase(n-2)
    res3 = staircase(n-3)
    return res1 + res2 + res3
    

# main
n = int(input())
print(staircase(n))

# ------------------------------------------------

# solution 2
def staircase(n,res=0):
    if (n < 3):
    	return n
    if (n == 3):
    	return 4
    return staircase(n-1) + staircase(n-2) + staircase(n-3)
    
# main
n = int(input())
print(staircase(n))