# Print Keypad

# Given an integer n, using phone keypad find out and print all the possible strings that can be made using digits of input n.
# Note : The order of strings are not important. Just print different strings in new lines.
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

# ---------------------------------------------------------------------------------

# solution:
button = {0:"",1:"",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
def printKeypad(n,ans):
    if n == 0 or n == 1:
        print(ans)
        return
    smallInt = n // 10
    currentNum = n % 10
    for s in button[currentNum]:
        printKeypad(smallInt,s+ans)
        
        
n = int(input())
printKeypad(n,"")