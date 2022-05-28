# Remove X

# Given a string, compute recursively a new string where all 'x' chars have been removed.
# Input format :
# String S
# Output format :
# Modified String

# Constraints :
# 1 <= |S| <= 10^3
# where |S| represents the length of string S. 

# Sample Input 1 :
# xaxb
# Sample Output 1:
# ab

# Sample Input 2 :
# abc
# Sample Output 2:
# abc

# Sample Input 3 :
# xx
# Sample Output 3:

# ***************************************************************************

# solution 1
def removeX(string):
    if len(string) == 0:
        return ""
    smallOutput = removeX(string[1:])
    if string[0] == 'x':
        return smallOutput
    else:
        return string[0]+smallOutput

# Main
string = input()
print(removeX(string))


# solution 2
def removeX(string):
    if len(string) == 0:
        return ""
    smallOutput = removeX(string[1:])
    if string[0] == 'x':
        return smallOutput
    else:
        return string[0]+smallOutput

# Main
string = input()
print(removeX(string))


# solution 3
def removeX(string):
    if len(string) == 0:
        return string
    smallOutput = removeX(string[1:])
    if string[0] == 'x':
        return smallOutput
    else:
        return string[0]+smallOutput

# Main
string = input()
print(removeX(string))
