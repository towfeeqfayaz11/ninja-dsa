# Alpha Pattern

# Print the following pattern for the given N number of rows.

# Pattern for N = 3
#  A
#  BB
#  CCC

# Input format :
# Integer N (Total no. of rows)

# Output format :
# Pattern in N lines

# Constraints
# 0 <= N <= 26

# Sample Input 1:
# 7
# Sample Output 1:
# A
# BB
# CCC
# DDDD
# EEEEE
# FFFFFF
# GGGGGGG

# Sample Input 2:
# 6
# Sample Output 2:
# A
# BB
# CCC
# DDDD
# EEEEE
# FFFFFF

# ***********************************************************************************************

# solution:
for i in range(int(input())):
    cp = 65+i
    for j in range(i+1):
        print(chr(cp),end='')
    print()


# solution
for i in range(1,int(input())+1):
    var = 64+i
    for _ in range(i):
        print(chr(var),end='')
    print()
        