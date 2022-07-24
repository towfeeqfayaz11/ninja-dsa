# Does s contain t ?

# Given two string s and t, write a function to check if s contains all characters of t (in the same order as they are in string t).
# Return true or false.
# Do it recursively.
# E.g. : s = “abchjsgsuohhdhyrikkknddg” contains all characters of t=”coding” in the same order. So function will return true.
# Input Format :
# Line 1 : String s
# Line 2 : String t
# Output Format :
# true or false
# Sample Input 1 :
# abchjsgsuohhdhyrikkknddg
# coding
# Sample Output 1 :
# true
# Sample Input 2 :
# abcde
# aeb
# Sample Output 2 :
# false


# solution:
def contains(s,t):
    #Implement This Function Here
    if len(t) == 0:
        return True
    if len(s) == 0:
        return False
    
    if t[0] == s[0]:
        return contains(s[1:],t[1:])
    else:
        return contains(s[1:],t)
    
s = input()
t = input()

ans = contains(s,t)
if ans is True:
    print('true')
else:
    print('false')