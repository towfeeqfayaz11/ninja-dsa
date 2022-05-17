# Repeating numbers

# Print the following pattern for the given number of rows.

# Pattern for N = 3
# 1
# 23
# 4567

# Input format : N (Total no. of rows)

# Output format : Pattern in N lines

# Sample Input :
# 5
# Sample Output :
# 1
# 23 
# 4567
# 89123456
# 7891234567891234

# ************************************************************************************

# solution1:
n = int(input())

c=1
for i in range(0,n):
    j=1
    while j<=2**i:
        if c>9:
            c=1
        print(c,end='')
        c+=1
        j+=1
    print()
    
# ************************************************************************************

# solution2:
n=int(input())
k=1
for i in range(n):
    for j in range(pow(2,i)):
        print(k,end='')
        k+=1
        if(k>9):
            k=1
    print()

# ************************************************************************************