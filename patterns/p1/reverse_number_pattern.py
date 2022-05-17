# Code : Reverse Number Pattern
# Send Feedback
# Print the following pattern for the given N number of rows.

# Pattern for N = 4
# 1
# 21
# 321
# 4321

# Input format :
# Integer N (Total no. of rows)

# Output format :
# Pattern in N lines

# Constraints
# 0 <= N <= 50

# Sample Input 1:
# 5
# Sample Output 1:
# 1
# 21
# 321
# 4321
# 54321

# Sample Input 2:
# 6
# Sample Output 2:
# 1
# 21
# 321
# 4321
# 54321
# 654321

# ****************************************************************************

# solution
for i in range(1,int(input())+1):
    j=i
    while j>0:
        print(j,end='')
        j-=1
    print()


# solution 2:
for i in range(1,int(input())+1):
    j = i
    while(j):
        print(j,end='')
        j-=1
    print()

# solution 3:
for i in range(1,int(input())+1):
    s = [str(j) for j in range(i,0,-1)]
    print("".join(s))