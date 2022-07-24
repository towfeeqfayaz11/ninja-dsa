# NOTE:
# in python to convert character to ascii and vice versa we use two functions ord() and chr()
# character to ascii     --> use ord()   --> gives ascii value corrsponding to a character   --> will work only for single length strings or in other words, a character
# ascii to character     --> useer chr() --> gives single character corresponding to an ascii value

# e.g;
# >>> ascii = 82
# >>> chr(ascii)
# 'R'

# >>> s = 'Python'
# >>> [ord(c) for c in s]
# [80, 121, 116, 104, 111, 110]

# ASCII range for english alphabets
# A - Z  --> 65 to 90
# a - z  --> 97 to 122


# to convert capital to small    --> add 32 to ascii value
# to convert small to capital    --> subtract 32 from ascii value

# e.g;
# >>> s1='a'
# >>> ord(s1)
# 97
# >>> chr(ord(s1)-32)
# 'A'
#########################################################################################################################################

Code : Character Pattern
Send Feedback
Print the following pattern for the given N number of rows.
Pattern for N = 4
A
BC
CDE
DEFG

Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines

Constraints
0 <= N <= 13

Sample Input 1:
5

Sample Output 1:
A
BC
CDE
DEFG
EFGHI

Sample Input 2:
6

Sample Output 2:
A
BC
CDE
DEFG
EFGHI
FGHIJK

# ********************************************************************************************************************************

# solution 1:
n = int(input())

for i in range(1,n+1):
    j = 1
    cp = 65+i-1
    while j <= i:
        print(chr(cp+j-1),end='')
        j+=1
    print()

# solution 2:
n = int(input())
for i in range(n):
    s = 65+i
    for j in range(s,s+i+1):
        print(chr(j), end='')
    print()
