# Code : Interesting Alphabets

# Print the following pattern for the given number of rows.

# Pattern for N = 5
# E
# DE
# CDE
# BCDE
# ABCDE

# Input format :
# N (Total no. of rows)

# Output format :
# Pattern in N lines

# Constraints
# 0 <= N <= 26

# Sample Input 1:
# 8

# Sample Output 1:
# H
# GH
# FGH
# EFGH
# DEFGH
# CDEFGH
# BCDEFGH
# ABCDEFGH

# Sample Input 2:
# 7

# Sample Output 2:
# G
# FG
# EFG
# DEFG
# CDEFG
# BCDEFG
# ABCDEFG

# ******************************************************************************************************

#solution 1:
n = int(input())

for i in range(n,0,-1):
    char_print = ord('A')+i-1
    j = 0
    while j<n-i+1:
        print(chr(char_print+j),end='')
        j+=1
    print()

# solution 2:
n = int(input())
last = 65+n-1
for i in range(n):
    for j in range(last-i,last+1):
        print(chr(j),end='')
    print()
    