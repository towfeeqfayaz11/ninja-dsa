# String to Integer

# Write a recursive function to convert a given string into the number it represents. That is input will be a numeric string that contains only numbers, you need to convert the string into corresponding integer and return the answer.
# Input format :
# Numeric string S (string, Eg. "1234")
# Output format :
# Corresponding integer N (int, Eg. 1234)
# Constraints :
# 0 <= |S| <= 9
# where |S| represents length of string S.
# Sample Input 1 :
# 00001231
# Sample Output 1 :
# 1231
# Sample Input 2 :
# 12567
# Sample Output 2 :
# 12567

# -------------------------------------------

# solution: (top down)
def string_to_integer(s,res):
    if len(s) == 0:
        return res
    res = res*10+int(s[0])
    output = string_to_integer(s[1:],res)       # string is passed first to last in top down approach
    return output
    

# main
s = input()
print(string_to_integer(s,0))

# ------------------------

# solution 2: (bottom up)
def string_to_integer(s):
    if len(s) == 0:
        return 0
    smallAns = string_to_integer(s[:-1])     # string is passed last to first in bottom up approach
    res = smallAns*10+int(s[-1])
    return res
    

# main
s = input()
print(string_to_integer(s))