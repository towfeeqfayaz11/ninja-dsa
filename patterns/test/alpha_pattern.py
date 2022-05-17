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

# *********************************************************************************
# solution 1:
for i in range(1,int(input())+1):
    print(chr(65+i-1)*i)

# *********************************************************************************

# solution 2:
n = int(input())

i=0
while i<n:
    j=0
    while j<=i:
        print(chr(65+i),end='')
        j+=1
    print()
    i+=1

# *********************************************************************************

# solution 3:
n = int(input())

i=0
while i<=n:
    j=0
    while j<i:
        print(chr(i+64),end='')
        j+=1
    print()
    i+=1
