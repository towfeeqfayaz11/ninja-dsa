# Number Pattern 2

# Print the following pattern for the given N number of rows.

# Pattern for N = 4
# 1
# 11
# 202
# 3003

# Input format :
# Integer N (Total no. of rows)

# Contraints:
# 1 <= n <= 50

# Output format :
# Pattern in N lines

# Sample Input :
# 5
# Sample Output :
# 1
# 11
# 202
# 3003
# 40004

# **********************************************************************************************

# solution 1:
for i in range(1,int(input())+1):
    if i == 1:
        print(1)
    else:
        print(i-1,'0'*(i-2),i-1,sep='')


# solutionn 2:
n = int(input())
for i in range(1,n+1):
    if i<=2:
        print('1'*i)
    else:
        print(str(i-1)+'0'*(i-2)+str(i-1))
    