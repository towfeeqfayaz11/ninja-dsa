# Number Pattern

# Print the following pattern for the given N number of rows.

# Pattern for N = 4
# 1234
# 123
# 12
# 1

# Input format :
# Integer N (Total no. of rows)

# Output format :
# Pattern in N lines

# Sample Input :
# 5
# Sample Output :
# 12345
# 1234
# 123
# 12
# 1

# **********************************************************************************************

# solution:
for i in range(int(input()),0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print()