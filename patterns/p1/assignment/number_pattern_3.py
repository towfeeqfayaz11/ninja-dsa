# Number Pattern 3

# Print the following pattern for the given N number of rows.

# Pattern for N = 4
# 1
# 11
# 121
# 1221

# Input format :
# Integer N (Total no. of rows)

# Output format :
# Pattern in N lines

# Sample Input :
# 5
# Sample Output :
# 1
# 11
# 121
# 1221
# 12221

# **********************************************************************************************

# solution 1:
for i in range(1,int(input())+1):
    if i<=2:
        print('1'*i)
    else:
        print('1'+'2'*(i-2)+'1')