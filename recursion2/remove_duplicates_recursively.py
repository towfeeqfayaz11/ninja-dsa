# Remove Duplicates Recursively

# Given a string S, remove consecutive duplicates from it recursively.
# Input Format :
# String S
# Output Format :
# Output string

# Constraints :
# 1 <= |S| <= 10^3
# where |S| represents the length of string

# Sample Input 1 :
# aabccba
# Sample Output 1 :
# abcba

# Sample Input 2 :
# xxxyyyzwwzzz
# Sample Output 2 :
# xyzwz

# ****************************************************************************

def removeConsecutiveDuplicates(string):
    if len(string) == 0 or len(string) == 1:
        return string
    
    smallOutput = removeConsecutiveDuplicates(string[1:])
    if string[0] == string[1]:
        return smallOutput
    else:
        return string[0]+smallOutput
    
    
# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
tsmt.rakuten-it.com