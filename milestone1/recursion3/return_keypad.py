# Return Keypad

# Given an integer n, using phone keypad find out and return all the possible strings that can be made using digits of input n.
# Note : The order of strings are not important.
# Input Format :
# Integer n
# Output Format :
# All possible strings in different lines
# Constraints :
# 1 <= n <= 10^6
# Sample Input:
# 23
# Sample Output:
# ad
# ae
# af
# bd
# be
# bf
# cd
# ce
# cf

# ------------------------------------------------------
 # solution 1:
 digits = {0:"",1:"",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}

def keypad(n):
    if n == 0 or n == 1:
        output = [""]
        return output
    smallInt = n // 10
    remainder = n % 10
    smallOutput= keypad(smallInt)
    output = []
    
    for s in digits[remainder]:
        for i in range(len(smallOutput)):
            output.append(smallOutput[i]+s)
    return output
    

n = int(input())
ans = keypad(n)
for s in ans:
    print(s)
# ----------------------------------------------------------

# solution 2: