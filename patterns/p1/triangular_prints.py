# print below patterns

# pattern: 1
# 1
# 1 2
# 1 2 3
# 1 2 3 4

# solution:
n = int(input())
for i in range(1,n+1):
    print(*(range(1,i+1)))

# solution:
n = int(input())
for i in range(1,n+1):
    j =1
    while j<=i:
        print(j,end='')
        j+=1
    print()

# **************************************************************************************

# pattern: 2
# 1
# 23
# 345
# 4567

# solution:
n = int(input())
for i in range(1,n+1):
    j = 0
    while j<i:
        print(i+j,end='')
        j+=1
    print()

# **************************************************************************************

# pattern: 3
# 1
# 23
# 456
# 78910

# solution:
n = int(input())
c=1
for i in range(1,n+1):
    for j in range(i):
        print(c,end='')
        c+=1
    print()