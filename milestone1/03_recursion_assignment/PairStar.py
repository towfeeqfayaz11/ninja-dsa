# Pair Star
# Given a string S, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".
# Input format :
# String S
# Output format :
# Modified string
# Constraints :
# 0 <= |S| <= 1000
# where |S| represents length of string S.
# Sample Input 1 :
# hello
# Sample Output 1:
# hel*lo
# Sample Input 2 :
# aaaa
# Sample Output 2 :
# a*a*a*a

# -----------------------------

# solution

def pair_star(s,si):
    if si == len(s) or si == len(s)-1:
        print(s)
        return
    
    if s[si] == s[si+1]:
        pair_star(s[:si+1]+"*"+s[si+1:],si+2)
    else:
        pair_star(s,si+1)


# main
s = input()
pair_star(s,0)