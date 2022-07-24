# Check Palindrome (recursive)

# Check whether a given String S is a palindrome using recursion. Return true or false.
# Input Format :
# String S
# Output Format :
# 'true' or 'false'
# Constraints :
# 0 <= |S| <= 1000
# where |S| represents length of string S.
# Sample Input 1 :
# racecar
# Sample Output 1:
# true
# Sample Input 2 :
# ninja
# Sample Output 2:
# false

# --------------------------------------------------

# solution
def check_palindrome(string):
    if len(string) == 0:
        return True
    
    if string[0] == string[-1]:
        return check_palindrome(string[1:-1])
    else:
        return False
    
s = input()
if check_palindrome(s):
    print('true')
else:
    print('false')