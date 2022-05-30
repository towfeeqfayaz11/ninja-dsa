# Terms of AP

# Write a program to print first x terms of the series 3N + 2 which are not multiples of 4.

# Input format :
# Integer x

# Output format :
# Terms of series (separated by space)

# Constraints :
# 1 <= x <= 1,000

# Sample Input 1 :
# 10
# Sample Output 1 :
# 5 11 14 17 23 26 29 35 38 41

# Sample Input 2 :
# 4
# Sample Output 2 :
# 5 11 14 17

# ************************************************************************************

# solution1:
n = int(input())
N=1
while n>0:
    if (3*N+2) %4 == 0:
        N+=1
    else:
        print(3*N+2,end=' ')
        n-=1
        N+=1

# ************************************************************************************

# solution2:
x= int(input())
n=1
m=0
while True:
    if m==x:
        break
    if (((3*n)+2) % 4) != 0:
        print((3*n)+2,end=' ')
        m+=1
    n+=1
    
# ************************************************************************************