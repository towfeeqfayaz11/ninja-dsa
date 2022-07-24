# Balanced Paranthesis

# For a given a string expression containing only round brackets or parentheses, check if they are balanced or not. 
# Brackets are said to be balanced if the bracket which opens last, closes first.

# Example:
# Expression: (()())
# Since all the opening brackets have their corresponding closing brackets, we say it is balanced and hence the output will be, 'true'.
# You need to return a boolean value indicating whether the expression is balanced or not.
# Note:
# The input expression will not contain spaces in between.
# Input Format:
# The first and the only line of input contains a string expression without any spaces in between.
#  Output Format:
# The only line of output prints 'true' or 'false'.
# Note:
# You don't have to print anything explicitly. It has been taken care of. Just implement the function. 
# Constraints:
# 1 <= N <= 10^7
#  Where N is the length of the expression.

# Time Limit: 1sec
# Sample Input 1 :
# (()()())
# Sample Output 1 :
# true
# Sample Input 2 :
# ()()(()
# Sample Output 2 :
# false
# Explanation to Sample Input 2:
# The initial two pairs of brackets are balanced. But when you see, the opening bracket at the fourth index 
# doesn't have its corresponding closing bracket which makes it imbalanced and in turn, making the whole expression imbalanced. 
# Hence the output prints 'false'.

#########################################################################################################

# solution 1:

from sys import stdin


def isBalanced(expression) :
    stack = []       # implementing stack using list
    for c in expression:
        if c == "(":
            stack.append(c)
        elif stack and c == ")" and stack[-1] == "(":   # stack is not empty, c is ) and the last ele in stack is (
            stack.pop()
    
    return len(stack) == 0
             


#main
expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")

else :
	print("false")




##########################################################################################################

# solution 2:
# TC = O(n), SC = O(n)
from sys import stdin


def isBalanced(expression) :
    stack = []       # implementing stack using list
    
    for i in expression:
        if i == "(":
            stack.append(i)
        elif i == ")" and len(stack) !=0 and stack[-1] == "(":
            stack.pop()
        else:
            pass
    
    return len(stack) == 0




#main
expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")

else :
	print("false")


##########################################################################################################

# solution 3:

from sys import stdin


def isBalanced(expression) :
    stack = []       # implementing stack using list
    for c in expression:
        if c == "(":
            stack.append(c)
        elif c == ")":
        	if (not stack):
        		return False
        	elif stack[-1] != "(":
        		return False
        	stack.pop()
    
    return len(stack) == 0
             


#main
expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")

else :
	print("false")
