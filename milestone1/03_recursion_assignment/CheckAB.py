# Check AB

# Suppose you have a string, S, made up of only 'a's and 'b's. Write a recursive function that checks if the string was generated using the following rules:
# a. The string begins with an 'a'
# b. Each 'a' is followed by nothing or an 'a' or "bb"
# c. Each "bb" is followed by nothing or an 'a'
# If all the rules are followed by the given string, return true otherwise return false.
# Input format :
# String S
# Output format :
# 'true' or 'false'
# Constraints :
# 1 <= |S| <= 1000
# where |S| represents length of string S.
# Sample Input 1 :
# abb
# Sample Output 1 :
# true
# Sample Input 2 :
# abababa
# Sample Output 2 :
# false
# Explanation for Sample Input 2
# In the above example, a is not followed by either "a" or "bb", instead it's followed by "b" which results in false to be returned.

# -----------------------------------------

# solution:
def check_AB(s):
    if  s == "abb" or s == "a":
        return True
    
    if s[0] == 'a':
        if s[:3] == "abb":
            return check_AB(s[3:])
        else:
            return check_AB(s[1:])
    else:
        return False


# main
s = input()
if check_AB(s):
    print('true')
else:
    print('false')

# solution 2:
def check_AB(s):
    if  len(s) == 0:
        return True
    
    if s[0] == 'a':
        if len(s[1:]) > 1 and str[1:3] == "bb":
            return check_AB(s[3:])
        else:
            return check_AB(s[1:])
    else:
        return False


s = input()

if check_AB(s):
    print('true')
else:
    print('false')